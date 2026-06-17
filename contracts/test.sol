pragma solidity ^0.7.0;

contract OverflowTest {

    uint256 balance;

    function addFunds(uint256 amount) public {
        balance = balance + amount;
    }
}