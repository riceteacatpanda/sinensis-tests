# sinensis-tests
Tests for the Sinensis API to determine which technology is best to use

### Test points

* Test JWT RS256 token generation
* Test JWT RS256 token read
* Test SQL insert
* Test SQL read

### Methodology

An API is run on the local machine and a Python script concurrently runs multiple requests against each endpoint, timing the length of time it takes for each to return. These are then averaged.

### Endpoints

* `/jwt/generate`
* `/jwt/read`
* `/sql/insert`
* `/sql/select`

### Libraries

**Go** - Mux, [dgrijalva/jwt-go](https://github.com/dgrijalva/jwt-go), built in SQL library

**Python** - Flask, PyJWT, `mysql.connector`

**Node.JS** - Express.JS, `jsonwebtoken`, `mysql`

### Bits of data

The JWT token that should be validated:

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIiLCJuYmYiOjE1OTE2OTgxMjR9.fphVmklaDmYxaBPAvrRKA8tFqumSt5s365llP0gY1jacbzFeH52TatL8ADXu5PuKHcVtHXKKlQ0Xldf3G6vB8XqlgsFrIxb1E2td64K8nufdxelNpF9GvSxBnA3lcqt4rOh1U2Bg54O2EoFr_kFR8QcTG6uhih_6nyYmlalxxWBUmzl796g2-B0pLCreXzqxAZGBbPDvoI4V5SclAwIg5n3zo3VOQPL87ztRkBRsQZjPIFoqeRc8tBvDYtpMbhZ7XaX-CmzZt4jQYNjWKbpn02QD6NAO0tmBPTC0D4s8uFLrRT65FYk625yLAu2wHWLaV4NeWz3Boent6O1-HVfLr8D7CTtmzucd_CsWb_Zyq5kplRhCC5-LPAQj0JH_WvDSn08lcQSZ37imU8tYEPiLGLB6-u5UA4y5HqzXgI1qqdQCU8dL0o64UyuiPZD4hkv3kSgc532jD0jQq24mRWxj9GUKH1Y0wSe263Y54UEkA0RbsunRFXepsdZATVc7u3s4PPrzAmIyr-TK1pGQtBKWXkqjD0hU2dCqW7eLj61nAe3tuzXQRh9iYeSyFZsicoK6VCbRNeAfm48c_FJOGTU5KOiDRnY441_fAlTQwNqFLoRcUm1paDm0xlrCO_B68j-FGdrbaqIgF-Io20aFFNj0UEOydiGXZ89tkImzisu4i14
```

Any JWT token that is generated should have the claim `"foo":"bar"` and `"nbf":1591698124`.

SQL user/password is `st-user`/`st-user`.

SQL database should be on `localhost:3306`.

SQL tests should use a parameterised query.

SQL insert should insert into database `sinensis-test`, table `inserttest`, column `number` with a random number between 1 and 100.

SQL read should read from the database `sinensis-test`, table `readtest`.

### Results

**50 requests per endpoint**

```
--- RESULTS ---
Golang
 jwt/generate/: 0.021885490417480467 seconds per request
 jwt/read/: 0.010388288497924805 seconds per request
 sql/insert/: 0.010767254829406738 seconds per request
 sql/select/: 0.009490714073181153 seconds per request
Average time per request: 0.01313293695449829 seconds

JavaScript
 jwt/generate/: 0.023129725456237794 seconds per request
 jwt/read/: 0.021802611351013183 seconds per request
 sql/insert/: 0.024572420120239257 seconds per request
 sql/select/: 0.020463895797729493 seconds per request
Average time per request: 0.022492163181304932 seconds

Python
 jwt/generate/: 0.027037138938903808 seconds per request
 jwt/read/: 0.014032306671142579 seconds per request
 sql/insert/: 0.024165077209472655 seconds per request
 sql/select/: 0.0225894832611084 seconds per request
Average time per request: 0.02195600152015686 seconds
```

**200 requests per endpoint**

```
--- RESULTS ---
Golang
 jwt/generate/: 0.021664707660675048 seconds per request
 jwt/read/: 0.009906940460205078 seconds per request
 sql/insert/: 0.010605031251907348 seconds per request
 sql/select/: 0.009961823225021363 seconds per request
Average time per request: 0.01303462564945221 seconds

JavaScript
 jwt/generate/: 0.019264423847198488 seconds per request
 jwt/read/: 0.01824252724647522 seconds per request
 sql/insert/: 0.01926470398902893 seconds per request
 sql/select/: 0.018711960315704344 seconds per request
Average time per request: 0.018870903849601744 seconds

Python
 jwt/generate/: 0.020502327680587767 seconds per request
 jwt/read/: 0.01235354781150818 seconds per request
 sql/insert/: 0.015815123319625854 seconds per request
 sql/select/: 0.015130118131637574 seconds per request
Average time per request: 0.015950279235839845 seconds
```

**400 requests per endpoint**

```
--- RESULTS ---
Golang
 jwt/generate/: 0.022289502024650572 seconds per request
 jwt/read/: 0.01029155969619751 seconds per request
 sql/insert/: 0.011018245220184327 seconds per request
 sql/select/: 0.010410805940628052 seconds per request
Average time per request: 0.013502528220415115 seconds

JavaScript
 jwt/generate/: 0.020287936329841615 seconds per request
 jwt/read/: 0.019038857817649843 seconds per request
 sql/insert/: 0.02035028338432312 seconds per request
 sql/select/: 0.019712246656417846 seconds per request
Average time per request: 0.019847331047058107 seconds

Python
 jwt/generate/: 0.021781071424484252 seconds per request
 jwt/read/: 0.01286419689655304 seconds per request
 sql/insert/: 0.01682237446308136 seconds per request
 sql/select/: 0.016164163947105407 seconds per request
Average time per request: 0.016907951682806014 seconds
```

**1000 requests per endpoint**

```
--- RESULTS ---
Golang
 jwt/generate/: 0.023944092988967894 seconds per request
 jwt/read/: 0.010461218595504761 seconds per request
 sql/insert/: 0.013272780656814575 seconds per request
 sql/select/: 0.011111929893493652 seconds per request
Average time per request: 0.014697505533695221 seconds

JavaScript
 jwt/generate/: 0.021845391511917115 seconds per request
 jwt/read/: 0.02035905146598816 seconds per request
 sql/insert/: 0.022200391054153442 seconds per request
 sql/select/: 0.021196373224258422 seconds per request
Average time per request: 0.021400301814079283 seconds

Python
 jwt/generate/: 0.024537539958953858 seconds per request
 jwt/read/: 0.014199618577957153 seconds per request
 sql/insert/: 0.02001341438293457 seconds per request
 sql/select/: 0.018767702102661134 seconds per request
Average time per request: 0.01937956875562668 seconds
```

**10,000 requests per endpoint**

```
--- RESULTS ---
Golang
 jwt/generate/: 0.016423852467536925 seconds per request
 jwt/read/: 0.006015836048126221 seconds per request
 sql/insert/: 0.007644516229629516 seconds per request
 sql/select/: 0.006612047123908997 seconds per request
Average time per request: 0.009174062967300415 seconds

JavaScript
 jwt/generate/: 0.014682369685173035 seconds per request
 jwt/read/: 0.012418719816207886 seconds per request
 sql/insert/: 0.015203924441337585 seconds per request
 sql/select/: 0.01483659222126007 seconds per request
Average time per request: 0.014285401540994645 seconds

Python
 jwt/generate/: 0.013394786834716796 seconds per request
 jwt/read/: 0.005096484971046447 seconds per request
 sql/insert/: 0.0320754653930664 seconds per request
 sql/select/: 0.030087527966499328 seconds per request
Average time per request: 0.020163566291332244 seconds
```

### Start commands for individual services

* Go: `cd go-api; go run main.go`
* JavaScript: `cd node-api; node index.js`
* Python: `cd python-api; pipenv run app`

### Test command

*All services must be started as well as a MySQL database prior to running the test script*

`cd tester; pipenv run python main.py`