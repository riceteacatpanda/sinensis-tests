# sinensis-tests
Tests for the Sinensis API

### Test points

* Test JWT asymmetric token generation
* Test JWT asymmetric token read
* Test SQL insert
* Test SQL read

### Methodology

An API is run on the local machine and a Python script runs 50-100 requests against each endpoint, timing the length of time it takes for each to return. These are then averaged.

### Endpoints

* `/jwt/generate`
* `/jwt/read`
* `/sql/insert`
* `/sql/read`

### Libraries

**Go** - Mux, [dgrijalva/jwt-go](https://github.com/dgrijalva/jwt-go)

**Python** - Flask, PyJWT

**Node.JS** - Express.JS, jsonwebtoken