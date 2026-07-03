pragma solidity ^0.8.0;

contract Bank {

    address owner;

    mapping(address => uint) balances;

    function deposit(uint amount) public payable {

    }

    function withdraw(uint amount) public {

    }

    function emergencyWithdraw() public onlyOwner {

    }
}