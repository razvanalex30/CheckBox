*** Settings ***
Library     SeleniumLibrary
Library    check_box.CheckBox
Library    BuiltIn
*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

*** Variables ***
${url}    https://demoqa.com/checkbox
@{values_list}    Private     Public    Angular
${browser}    chrome

*** Test Cases ***
TestCheckbox
    Open Browser Page
    Find Checkboxes
    Check Selected    ${values_list}
    Sleep   5
    Close Browser