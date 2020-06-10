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
 jwt/generate/: 0.02212080955505371 seconds per request
 jwt/read/: 0.010511775016784668 seconds per request
 sql/insert/: 0.011090307235717774 seconds per request
 sql/select/: 0.009773812294006347 seconds per request
Average time per request: 0.013374176025390625

JavaScript
 jwt/generate/: 0.01930830955505371 seconds per request
 jwt/read/: 0.01633559226989746 seconds per request
 sql/insert/: 0.019347538948059084 seconds per request
 sql/select/: 0.018669567108154296 seconds per request
Average time per request: 0.018415251970291136

Python
 jwt/generate/: 0.02579103946685791 seconds per request
 jwt/read/: 0.015957350730895995 seconds per request
 sql/insert/: 0.021622347831726074 seconds per request
 sql/select/: 0.02050506114959717 seconds per request
Average time per request: 0.020968949794769286
```

**200 requests per endpoint**

```
--- RESULTS ---
Golang
 jwt/generate/: 0.021033886671066284 seconds per request
 jwt/read/: 0.009684100151062011 seconds per request
 sql/insert/: 0.010322383642196654 seconds per request
 sql/select/: 0.009639184474945068 seconds per request
Average time per request: 0.012669888734817504 seconds

JavaScript
 jwt/generate/: 0.018934531211853026 seconds per request
 jwt/read/: 0.017024459838867186 seconds per request
 sql/insert/: 0.018979417085647585 seconds per request
 sql/select/: 0.018420594930648803 seconds per request
Average time per request: 0.01833975076675415 seconds

Python
 jwt/generate/: 0.021557347774505617 seconds per request
 jwt/read/: 0.01299025297164917 seconds per request
 sql/insert/: 0.016695375442504882 seconds per request
 sql/select/: 0.015782628059387207 seconds per request
Average time per request: 0.01675640106201172 seconds
```

**400 requests per endpoint**

```
--- RESULTS ---
Golang
 jwt/generate/: 0.02097390055656433 seconds per request
 jwt/read/: 0.00946717917919159 seconds per request
 sql/insert/: 0.010075551867485046 seconds per request
 sql/select/: 0.009664133191108704 seconds per request
Average time per request: 0.012545191198587418 seconds

JavaScript
 jwt/generate/: 0.01850809872150421 seconds per request
 jwt/read/: 0.01755066156387329 seconds per request
 sql/insert/: 0.0185854172706604 seconds per request
 sql/select/: 0.018144344091415406 seconds per request
Average time per request: 0.018197130411863327 seconds

Python
 jwt/generate/: 0.02141772210597992 seconds per request
 jwt/read/: 0.012745919227600098 seconds per request
 sql/insert/: 0.01627397894859314 seconds per request
 sql/select/: 0.01552843689918518 seconds per request
Average time per request: 0.016491514295339585 seconds
```

### Start commands for individual services

* Go: `cd go-api; go run main.go`
* JavaScript: `cd node-api; node index.js`
* Python: `cd python-api; pipenv run app`

### Test command

*All services must be started as well as a MySQL database prior to running the test script*

`cd tester; pipenv run python main.py`