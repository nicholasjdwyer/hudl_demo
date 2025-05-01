# hudl_demo
Demo project for Hudl interview.

Scope:
Purpose of this project is to run a few simple tests for the hudl login page. 


To Run:
You will need python, selenium, and the most recent chrome and chrome web driver to run the suite. Additionally you will need to replace the below variables in the tests with your own creds to execute the tests. 

*UserName*
*PassWord*

Replace those with your own username and password in the .py file test data section you are running to execute tests. 

To Do:
-review hudl documentation to clean up IDE steps into more stable selection (like using testing specific tags if they exist) 
-create additional accounts in various states to check additional login scenarios (locked out, needing password reset, deleted or expired accounts) 
-add reporting so testing results can be more easily passed along 



interviewee thoughts:
Essentially this project is how I approach the first round of automation when working on tests for new sprint work. I build a quick set of tests with some simple framework, then use that basic test structure to expand to more complicated testing scenarios. During that process I also bring tests in line to whatever standard or test structure the project is utilizing at that time. Then any new variables are integrated to the test data and the tests are committed to the repository and documentation is created. 
