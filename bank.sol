pragma solidity ^0.8.0;

contract Bank {

    function withdraw(uint amount) public {

        msg.sender.call{value: amount}("");
    }
}