*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Ville
    Set Password  Ville123
    Set Password Confirmation  Ville123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  V
    Set Password  Ville123
    Set Password Confirmation  Ville123
    Click Button  Register
    Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Set Username  Ville1
    Set Password  abcd
    Set Password Confirmation  abcd
    Click Button  Register
    Register Should Fail With Message  Too short password

Register With Valid Username And Invalid Password
    Set Username  Ville1
    Set Password  abcdefghi
    Set Password Confirmation  abcdefghi
    Click Button  Register
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  Ville1234
    Set Password  Ville123
    Set Password Confirmation  Ville321
    Click Button  Register
    Register Should Fail With Message  Password and password confirmation don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  Ville123
    Set Password Confirmation  Ville123
    Click Button  Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
