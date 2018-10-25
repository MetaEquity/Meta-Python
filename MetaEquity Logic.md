# Meta-Python
Classes:
Token
Crowdfunding.
Inflation Dynamic distribution.
Dividends distribution.
Main ico contract
Price Oracle
General SC inputs
-META
-Metaquities
General SC methods:
1. Voting: voting weight is calculated in each contract after voting.
- get token ownership in the last x of time.
- any token pre-existed before x period of time is considered old enough.
- provided that a maturation time has passed, a function of tokens age + amount to get the voting weight.
- a sum of voting weight is calculated for each decision.
- each decision ID is the number of tokens sent to the contract.
- for each decision ID votes are limited to one/sender address.
- for each decision ID if the sum passes a threshold an owner permission is granted.
- optional: not all incoming transactions are considered as a vote, they must fulfil a criterion, like a being divisible by a number.
- setting a voting period, new voting ID and 
- the fair distribution factor, 

SC division and hierarchy. 
1. META SC:
a. Start new asset SC:
- made for votes to deploy a new token.
- set with voting parameters.
- has a voting bounty.

methods:
- refund voters.
- send voting bounty to voters.
- Calculate the voting decision.
- deploy target smart contracts.

b. Locked awards SC.
Inputs:
- votes.

Methods:
- all voting capabilities.
- wallets can request to unlock and get the award, mu


Standard metaquity token SC:
Token SC
Crowdfunding SC.
DDR SC:
- token supply= max supply-initial supply.
- wallets are hardcoded to request minting?

input: 
- token price in BTC/dollars
- token circulating supply.
- wallets minting requests.

Methods: 
- update the max supply according to the price and
- get tokens' age for each wallet requesting to mint.
- calculate staking weight according to a function.
- do exchange.

dividends distribution contract:
1. timed for each company to a distribution period.
2. No outside invokes.
3. input: 
- token price, market cap.
- token ownership in the last financial period.

methods: 
- exclude short ownerships/distribute the rest to long-term owners.
- monitor circulating supply growth.
- spread tokens temporally according to (distribution time && past circulation growth).
- update circulation growth and recalculate distribution.
- Optional: allow resetting of the distribution function.


External functions/libraries
get Price API
