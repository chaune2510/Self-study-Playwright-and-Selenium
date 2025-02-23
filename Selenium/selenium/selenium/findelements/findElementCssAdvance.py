"""
input[id=displayedtext]
#displayedtext
input#displayedtext

input[class=displayedclass]
.displayedclass
input.displayedclass

Appending Classes
.class1.class2.class3

Using Wildcards in CSS selector

^ -> thay the cho starting text
$ -> thay the cho ending text
* => thay the cho text

Syntax:
tag[attribute<special character>='value']

input[class='inputs'] -> only 1 matching node
input[class^='inputs'] -> only 2 matching node
input[class='displayed-class'] -> no matching node
input[class$='class'] -> one matching node
input[class*='displayed-class'] -> one matching node











XPath:
Syntax:
//tag[@attribute='value']
Using Text of the element to build xpath
Finding    Login    link:
//div[@class='homepage hero']//a[text()='Enroll now']

Using    Contains    to    find    the    elements:
Syntax:
//tag[contains(attribute, ‘value’)]
Finding    Login    link:
//div[@id='navbar']//a[contains(text(),'Login')]
//div[@id='navbar']//a[contains(@class,'navbar--link') and contains(@href,'sign_in')]
//td[@class='active day' and text()='25']


















"""