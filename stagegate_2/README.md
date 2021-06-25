# stagegate2 writeup

The encryption used is standard AES-128 with random jittering at the begining of the encryption. 
In order to recover the secret key processed using CPA attacks, the traces have to be aligned. 
The trace alignment is performed using numpy correlate function. 
