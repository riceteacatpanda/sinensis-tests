# sinensis-tests
Tests for the Sinensis API to determine which technology is best to use

### Test points

* Test JWT RS256 token generation
* Test JWT RS256 token read
* Test SQL insert
* Test SQL read

### Methodology

An API is run on the local machine and a Python script runs 50 requests against each endpoint, timing the length of time it takes for each to return. These are then averaged.

### Endpoints

* `/jwt/generate`
* `/jwt/read`
* `/sql/insert`
* `/sql/select`

### Libraries

**Go** - Mux, [dgrijalva/jwt-go](https://github.com/dgrijalva/jwt-go)

**Python** - Flask, PyJWT

**Node.JS** - Express.JS, jsonwebtoken

### Bits of data

The JWT token that should be validated:

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIiLCJuYmYiOjE1OTE2OTgxMjR9.fphVmklaDmYxaBPAvrRKA8tFqumSt5s365llP0gY1jacbzFeH52TatL8ADXu5PuKHcVtHXKKlQ0Xldf3G6vB8XqlgsFrIxb1E2td64K8nufdxelNpF9GvSxBnA3lcqt4rOh1U2Bg54O2EoFr_kFR8QcTG6uhih_6nyYmlalxxWBUmzl796g2-B0pLCreXzqxAZGBbPDvoI4V5SclAwIg5n3zo3VOQPL87ztRkBRsQZjPIFoqeRc8tBvDYtpMbhZ7XaX-CmzZt4jQYNjWKbpn02QD6NAO0tmBPTC0D4s8uFLrRT65FYk625yLAu2wHWLaV4NeWz3Boent6O1-HVfLr8D7CTtmzucd_CsWb_Zyq5kplRhCC5-LPAQj0JH_WvDSn08lcQSZ37imU8tYEPiLGLB6-u5UA4y5HqzXgI1qqdQCU8dL0o64UyuiPZD4hkv3kSgc532jD0jQq24mRWxj9GUKH1Y0wSe263Y54UEkA0RbsunRFXepsdZATVc7u3s4PPrzAmIyr-TK1pGQtBKWXkqjD0hU2dCqW7eLj61nAe3tuzXQRh9iYeSyFZsicoK6VCbRNeAfm48c_FJOGTU5KOiDRnY441_fAlTQwNqFLoRcUm1paDm0xlrCO_B68j-FGdrbaqIgF-Io20aFFNj0UEOydiGXZ89tkImzisu4i14
```

Any JWT token that is generated should have the claim `"foo":"bar"` and `"nbf":1591698124`.

SQL user/password is `st-user`/`st-user`.

SQL tests should use a parameterised query.

SQL insert should insert into database `sinensis-test`, table `inserttest`, column `number` with a random number between 1 and 100.

SQL read should read from the database `sinensis-test`, table `readtest`.

### Results

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

