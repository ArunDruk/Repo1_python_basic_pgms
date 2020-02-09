*** Settings ***
Documentation    Suite description
Library     SeleniumLibrary

****** Variables ***
${Browser}      Chrome
${URL}      https://www.pavanonlinetrainings.com


*** Test Cases ***
Login test
    Open Browser




*** Keywords ***
Provided precondition
