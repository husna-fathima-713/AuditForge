pragma solidity ^0.8.0;

contract Token {

    function mint(address user, uint amount) public {

    }
}

pragma solidity ^0.8.0;

contract Bank {

    function withdraw(uint amount) public {
        msg.sender.call{value: amount}("");
    }
}