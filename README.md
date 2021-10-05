# reqres-apis
Rest Endpoints Automation: https://reqres.in/


Run Tests:

Dependencies:
- Ensure you have atleast Python 3 & PyTest installed:  https://docs.pytest.org/en/6.2.x/getting-started.html
- Ensure you have Requests installed: https://docs.python-requests.org/en/latest/user/install/#python-m-pip-install-requests
- Ensure you have Faker installed:  https://pypi.org/project/Faker/
- Navigate to /tests after cloning the repo
- Run `pytest tests/ -s -v`

<img width="909" alt="Screen Shot 2021-10-05 at 2 26 16 PM" src="https://user-images.githubusercontent.com/22087224/136081289-b58c3169-022e-4290-bbfd-27bda01bf86a.png">

This is a sample mini API framwework: 

Pros:

- Provides a good modularization, easy test maintenance.
- Supports reusability
- Cost effective, PyTest and other modules are free
- Run multiple tests in parallel
- Easy to set up 
- Easy to read and allow collaborators to add more code 

Cons:
- Requires background & knowledge of PyTest in order to add to the framework 
- Tests can be repetitive to add on or to write 
