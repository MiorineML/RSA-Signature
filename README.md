# 427-RSA 

Sample output: <br />

In this case, p and q are hard coded. The program will randomly generate this. <br />

In "sign" mode: <br />
sign "hello, friend!" <br />
p = 9da5, q = b28b, n = 6df25297, t = 6df10268 <br />
received message: hello, friend! <br />
message hash: 1bcbce1 <br />
signing with the following private key: 4a5a9c39 <br />
signed hash: 18e1eac9 <br />
uninverted message to ensure integrity: 1bcbce1 <br />
complete output for verification: <br />
6df25297 "hello, friend!" 18e1eac9 <br />

In "verify" mode: <br />
verify 6df25297 "hello, friend!" 18e1eac9 <br />
message verified! <br />

In "verify" mode for a forged message: <br />
verify 6df25297 "hello, friend!" 18e1eac8 <br />
!!! message is forged !!! 
