package main

import (
	"crypto/rsa"
	"database/sql"
	"encoding/json"
	"io/ioutil"
	"log"
	"math/rand"
	"net/http"
	"strconv"

	"github.com/dgrijalva/jwt-go"
	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

var (
	pubKey  *rsa.PublicKey
	privKey *rsa.PrivateKey
	dbConn  *sql.DB
)

func checkError(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	log.Println("Go API test")

	log.Println("Loading RSA keys")

	pubKeyCont, err := ioutil.ReadFile("../public.key")
	checkError(err)
	pubKey, err = jwt.ParseRSAPublicKeyFromPEM([]byte(pubKeyCont))
	checkError(err)

	privKeyCont, err := ioutil.ReadFile("../private.key")
	checkError(err)
	privKey, err = jwt.ParseRSAPrivateKeyFromPEM([]byte(privKeyCont))
	checkError(err)

	log.Println("Connecting to database")

	dbConn, err = sql.Open("mysql", "st-user:st-user@tcp(127.0.0.1:3306)/sinensis-test")
	checkError(err)
	defer dbConn.Close()

	err = dbConn.Ping()
	checkError(err)

	r := mux.NewRouter()

	r.HandleFunc("/jwt/generate/", jwtGenerate)
	r.HandleFunc("/jwt/read/", jwtRead)
	r.HandleFunc("/sql/insert/", sqlInsert)
	r.HandleFunc("/sql/select/", sqlSelect)

	log.Fatal(http.ListenAndServe(":8000", r))
}

func jwtRead(w http.ResponseWriter, r *http.Request) {

	var tokenString = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIiLCJuYmYiOjE1OTE2OTgxMjR9.fphVmklaDmYxaBPAvrRKA8tFqumSt5s365llP0gY1jacbzFeH52TatL8ADXu5PuKHcVtHXKKlQ0Xldf3G6vB8XqlgsFrIxb1E2td64K8nufdxelNpF9GvSxBnA3lcqt4rOh1U2Bg54O2EoFr_kFR8QcTG6uhih_6nyYmlalxxWBUmzl796g2-B0pLCreXzqxAZGBbPDvoI4V5SclAwIg5n3zo3VOQPL87ztRkBRsQZjPIFoqeRc8tBvDYtpMbhZ7XaX-CmzZt4jQYNjWKbpn02QD6NAO0tmBPTC0D4s8uFLrRT65FYk625yLAu2wHWLaV4NeWz3Boent6O1-HVfLr8D7CTtmzucd_CsWb_Zyq5kplRhCC5-LPAQj0JH_WvDSn08lcQSZ37imU8tYEPiLGLB6-u5UA4y5HqzXgI1qqdQCU8dL0o64UyuiPZD4hkv3kSgc532jD0jQq24mRWxj9GUKH1Y0wSe263Y54UEkA0RbsunRFXepsdZATVc7u3s4PPrzAmIyr-TK1pGQtBKWXkqjD0hU2dCqW7eLj61nAe3tuzXQRh9iYeSyFZsicoK6VCbRNeAfm48c_FJOGTU5KOiDRnY441_fAlTQwNqFLoRcUm1paDm0xlrCO_B68j-FGdrbaqIgF-Io20aFFNj0UEOydiGXZ89tkImzisu4i14"

	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		return pubKey, nil
	})
	checkError(err)

	returnData := map[string]interface{}{
		"status":     "ok",
		"validToken": strconv.FormatBool(token.Valid),
	}
	jsonData, err := json.Marshal(returnData)
	checkError(err)

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(jsonData))

}

func jwtGenerate(w http.ResponseWriter, r *http.Request) {

	token := jwt.NewWithClaims(jwt.SigningMethodRS256, jwt.MapClaims{
		"foo": "bar",
		"nbf": 1591698124,
	})

	tokenString, err := token.SignedString(privKey)
	checkError(err)

	returnData := map[string]interface{}{
		"status": "ok",
		"token":  tokenString,
	}
	jsonData, err := json.Marshal(returnData)
	checkError(err)

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(jsonData))

}

func sqlInsert(w http.ResponseWriter, r *http.Request) {

	preparedStatement, err := dbConn.Prepare("INSERT INTO inserttest (`number`) VALUES( ? )")
	checkError(err)
	defer preparedStatement.Close()

	rNum := rand.Intn(100)

	_, err = preparedStatement.Exec(rNum)
	checkError(err)

	returnData := map[string]interface{}{
		"status": "ok",
		"number": strconv.FormatInt(int64(rNum), 10),
	}
	jsonData, err := json.Marshal(returnData)
	checkError(err)

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(jsonData))

}

func sqlSelect(w http.ResponseWriter, r *http.Request) {

	preparedStatement, err := dbConn.Prepare("SELECT age FROM readtest WHERE id = ?")
	checkError(err)
	defer preparedStatement.Close()

	var outputVal int
	err = preparedStatement.QueryRow(1).Scan(&outputVal)
	checkError(err)

	returnData := map[string]interface{}{
		"status": "ok",
		"age":    strconv.FormatInt(int64(outputVal), 10),
	}
	jsonData, err := json.Marshal(returnData)
	checkError(err)

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(jsonData))

}
