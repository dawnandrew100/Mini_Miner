# Mini Miner

This will be a solution to hackattic's "Mini miner" coding challenge

In this challenge a JSON is received from the endpoint with two attributes: block and difficulty. 
The block attribute contains data, which houses arbitrary data and nonce. 
The Mini Miner's goal is to find a nonce value that causes the SHA256 hash of block to start with difficulty zero bits. 
That is, if difficulty is 4, the hash should start with at least 4 zero bits.
