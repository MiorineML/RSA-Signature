# 427-RSA

Sample output:

In this case, p and q are hard coded. The program will randomly generate this.

In "sign" mode:
sign "hello, friend!"
p = 9da5, q = b28b, n = 6df25297, t = 6df10268
received message: hello, friend!
message hash: 1bcbce1
signing with the following private key: 4a5a9c39
signed hash: 18e1eac9
uninverted message to ensure integrity: 1bcbce1
complete output for verification:
6df25297 "hello, friend!" 18e1eac9

In "verify" mode:
verify 6df25297 "hello, friend!" 18e1eac9
message verified!

In "verify" mode for a forged message:
verify 6df25297 "hello, friend!" 18e1eac8
!!! message is forged !!!
