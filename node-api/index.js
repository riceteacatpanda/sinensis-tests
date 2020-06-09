const express = require("express")
const mysql = require("mysql")
const jwt = require("jsonwebtoken")
const fs = require("fs")

const app = express()
const port = 8001

const pubKey = fs.readFileSync("../public.key")
const privKey = fs.readFileSync("../private.key")

const dbConn = mysql.createConnection({
  host: "localhost",
  user: "st-user",
  password: "st-user",
  database : "sinensis-test"
})

dbConn.connect()

app.get("/jwt/generate", (req, res) => {
  
  const token = jwt.sign("{'foo':'bar','nbf':1591698124}", privKey, { algorithm: "RS256" })

  res.append("Content-Type", "application/json")
  return res.send(JSON.stringify({"status": "ok", "token": token}))
})

app.get("/jwt/read", (req, res) => {
  
  const tokenString = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIiLCJuYmYiOjE1OTE2OTgxMjR9.fphVmklaDmYxaBPAvrRKA8tFqumSt5s365llP0gY1jacbzFeH52TatL8ADXu5PuKHcVtHXKKlQ0Xldf3G6vB8XqlgsFrIxb1E2td64K8nufdxelNpF9GvSxBnA3lcqt4rOh1U2Bg54O2EoFr_kFR8QcTG6uhih_6nyYmlalxxWBUmzl796g2-B0pLCreXzqxAZGBbPDvoI4V5SclAwIg5n3zo3VOQPL87ztRkBRsQZjPIFoqeRc8tBvDYtpMbhZ7XaX-CmzZt4jQYNjWKbpn02QD6NAO0tmBPTC0D4s8uFLrRT65FYk625yLAu2wHWLaV4NeWz3Boent6O1-HVfLr8D7CTtmzucd_CsWb_Zyq5kplRhCC5-LPAQj0JH_WvDSn08lcQSZ37imU8tYEPiLGLB6-u5UA4y5HqzXgI1qqdQCU8dL0o64UyuiPZD4hkv3kSgc532jD0jQq24mRWxj9GUKH1Y0wSe263Y54UEkA0RbsunRFXepsdZATVc7u3s4PPrzAmIyr-TK1pGQtBKWXkqjD0hU2dCqW7eLj61nAe3tuzXQRh9iYeSyFZsicoK6VCbRNeAfm48c_FJOGTU5KOiDRnY441_fAlTQwNqFLoRcUm1paDm0xlrCO_B68j-FGdrbaqIgF-Io20aFFNj0UEOydiGXZ89tkImzisu4i14"
  const decodedToken = jwt.verify(tokenString, pubKey, { algorithms: ["RS256"] })

  res.append("Content-Type", "application/json")
  return res.send(JSON.stringify({"status": "ok", "validToken": true}))
})

app.get("/sql/insert", (req, res) => {
  
  const randomNumber = Math.floor(Math.random() * Math.floor(100))

  dbConn.query('INSERT INTO inserttest (`number`) VALUES ( ? )', [randomNumber], function (error, results, fields) {
    if (error) throw error;

    res.append("Content-Type", "application/json")
    return res.send(JSON.stringify({"status": "ok", "number": randomNumber}))

  });
})

app.get("/sql/select", (req, res) => {
  
  dbConn.query('SELECT age FROM readtest WHERE id = ?', [1], function (error, results, fields) {
    if (error) throw error;

    res.append("Content-Type", "application/json")
    return res.send(JSON.stringify({"status": "ok", "age": results[0].age}))

  });
})

app.listen(port, () => console.log(`Node API test at http://localhost:${port}`))
