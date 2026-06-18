pragma solidity ^0.8.0;

contract Token {

    mapping(address => uint256) balances;

    function mint(address user, uint256 amount) public {
        balances[user] += amount;
    }
}