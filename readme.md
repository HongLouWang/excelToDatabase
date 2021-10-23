# Excel To Database

Prepared by:

* `Shutian Wang`

----
## Use Cases
| Use case # 1      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Name              | **Create MySQL Database Connection**   |
| Users             | User User                                                 |
| Rationale         | User Create MySQL Database Connection |
| Triggers          | User type in command|
| Preconditions     | Program start |
| Actions           | 1. Program catch user inputed database type, host address, username, password, port and database name. <br >2. Program init mysql database connection and catch the database object. |
| Alternative paths | 1. If user didn't type in database information, return and notice the user.<br />2. If the database information is not vaild, return and notice the user database information not valid.|
| Postconditions    | Program init mysql connection and catch the database object|
| Acceptance tests  | Make sure the database connected successfully! |
| Iteration         | **#1**                                                       |

| Use case # 2      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Name              | **Init excel workbook and worksheet**   |
| Users             | User User                                                 |
| Rationale         | User Create MySQL Database Connection |
| Triggers          | User type in command|
| Preconditions     | Program start |
| Actions           | 1. Program catch user inputed excel filename, filepath and worksheet name <br >2. Program load user inputed excel file |
| Alternative paths | 1. If user didn't type in excel information, return and notice the user.<br />2. If the excel filename, filepath or worksheet not valid, return and notice the user filename, filepath or worksheet not valid|
| Postconditions    | Program init mysql connection and catch the database object|
| Acceptance tests  | Make sure the database connected successfully! |
| Iteration         | **#1**                                                       |


----
## TODO
| TODO Task # 1      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **1**   |
| User case         | 1 User                                                 |
| Rationale         | The Users have the access to create account in faculty page by filling the required profile information. The Create a Faculty Account and Enter Profile Information should allows Users to create a login and become a Registered User. |
| Triggers          | The faculty user select the "Create Account" option          |
| Preconditions     | The form and the model of the database have been successfully created |
| Actions           | 1. The Users enter the required Faculty Account information values and requests that the system saves the entered values.<br />2. The system validates the entered Faculty Account information and Profile Information<br />3. The entered data for the Users information are stored in the User's account.<br />4. The system notifies the User that the account has been created<br /> |
| Alternative paths | 1. The User can choose to cancel create the account at any time.<br />2. In step 2, the system describes which entered data was invalid and presents the User with suggestions for entering valid data.<br />3. In step 2, the User re-enters the information and the system re-validates it.<br />4. In step 2, if the invalid values is entered, the entered information is invalid alternative flow is executed again. This continues until the users chose to cancel create the account. |
| Postconditions    | The User entered data is stored in the user account.         |
| Acceptance tests  | Make sure that all the User entered data is valid and successfully stored in the system. |
| Iteration         | **#1**                                                       |
