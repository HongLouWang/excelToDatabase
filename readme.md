# Excel To Database

Prepared by:

* `Shutian Wang`

----
## Use Cases
| Use case # 1      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Name              | **Create MySQL Database Connection**   |
| Users             | User                                                  |
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
| Users             | User                                                  |
| Rationale         | User load excel workbook |
| Triggers          | User type in command|
| Preconditions     | Program start |
| Actions           | 1. Program catch user inputed excel filename, filepath and worksheet name <br >2. Program load user inputed excel file |
| Alternative paths | 1. If user didn't type in excel information, return and notice the user.<br />2. If the excel filename, filepath or worksheet not valid, return and notice the user filename, filepath or worksheet not valid|
| Postconditions    | Program init mysql connection and catch the database object|
| Acceptance tests  | Make sure the excel file user inputed loaded successfully! |
| Iteration         | **#1**                                                       |

| Use case # 3      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Name              | **Insert excel to mysql database**   |
| Users             | User                                                  |
| Rationale         | Insert user inputed excel file to database |
| Triggers          | User type in command|
| Preconditions     | Program start, database connection establishment, excel file and worksheet exist |
| Actions           | 1. Read user inputed excel worksheet line by line <br >2. Insert each line into database |
| Alternative paths | 1. If database connection not established, return and notice the user.<br >2. if the user inputed excel file or worksheet not exist, return and notice the user.<br >3. In step 2, if data cannot insert into database, return and notice the user which line throw error.|
| Postconditions    | User selected excel file inserted into database|
| Acceptance tests  | Make sure the excel file inserted into the database successfully! |
| Iteration         | **#1**                                                       |

| Use case # 4      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Name              | **Insert partal excel worksheet into database**   |
| Users             | User                                                  |
| Rationale         | Let user input the excel range, insert the range of excel worksheet into datbase |
| Triggers          | User type in command|
| Preconditions     | Program start, database connection establishment, excel file and worksheet exist, user inputed excel worksheet exist in workbook |
| Actions           | 1. Read user inputed excel worksheet range and convert it to openpyxl understandable range. <br >2. Insert each line into database |
| Alternative paths | 1. If database connection not established, return and notice the user.<br >2. If the user inputed excel file or worksheet not exist, return and notice the user.<br >3. If the user inputed excel worksheet range is not exist or out of range, return and notice the user.<br >4. In step 2, if data cannot insert into database, return and notice the user which line throw error.|
| Postconditions    | User selected excel worksheet range inserted into database|
| Acceptance tests  | Make sure the excel worksheet range inserted into the database successfully! |
| Iteration         | **#2**                                                       |

| Use case # 5      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Name              | **Insert excel data by user inputed dictionary**   |
| Users             | User                                                  |
| Rationale         | Let user input a dictionary, then insert the data from excel worksheet to the database by user inputed dictionary |
| Triggers          | User type in command|
| Preconditions     | Program start, database connection establishment, excel file and worksheet exist, user inputed dictionary matched each other |
| Actions           | 1. Read user inputed dictionary <br >2. Insert the data from worksheet by dictionary- |
| Alternative paths | 1. If database connection not established, return and notice the user.<br >2. If the user inputed excel file or worksheet not exist, return and notice the user.<br >3. If the user inputed dictionary does not match each other, return and notice the user.<br >4. In step 2, if data cannot insert into database, return and notice the user which line throw error.|
| Postconditions    | User selected excel worksheet range inserted into database by user inputed dictionary|
| Acceptance tests  | Make sure the excel worksheet range inserted into the database by user inputed dictionary successfully! |
| Iteration         | **#2**                                                       |


----
## TODO
| TODO Task # 1      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **1**   |
| User case         | 1 User                                                 |
| Create date       | 2021-10-18 |
| Creator           | Shutian Wang |
| Assign date       | 2021-10-18 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Program catch user inputed database information, check database information inputed or not. If not, return and notice user.|

| TODO Task # 2      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **1**   |
| User case         | 1                                       |
| Create date       | 2021-10-18 |
| Creator           | Shutian Wang |
| Assign date       | 2021-10-18 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Connect database, check user credential, if connection success, save mysql connection object.|

| TODO Task # 3      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **1**   |
| User case         | 2                                       |
| Create date       | 2021-10-18 |
| Creator           | Shutian Wang |
| Assign date       | 2021-10-18 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Program catch user inputed excel excel file and worksheet information, check if the excel file exist and the worksheet exist. If excel file or worksheet not exist, return and notice the user. If excel file and worksheet exist, load and save the excel object.|

| TODO Task # 4      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **1**   |
| User case         | 3                                       |
| Create date       | 2021-10-18 |
| Creator           | Shutian Wang |
| Assign date       | 2021-10-18 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Program read user input excel file line by line, then insert that line into database.|

| TODO Task # 5      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **2**   |
| User case         | 4                                       |
| Create date       | 2021-10-25 |
| Creator           | Shutian Wang |
| Assign date       | 2021-10-25 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Program read user input excel worksheet range, convert it to excel worksheet range understand by openpyxl.|

| TODO Task # 6      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **2**   |
| User case         | 4                                       |
| Create date       | 2021-10-25 |
| Creator           | Shutian Wang |
| Assign date       | 2021-10-25 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Read the excel worksheet data which selected by the user, Insert it to the database line by line.|

| TODO Task # 7      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **2**   |
| User case         | 5                                       |
| Create date       | 2021-10-26 |
| Creator           | Shutian Wang |
| Assign date       | 2021-10-26 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Read the dictionary inputed by user, assemble sql query and insert to the database line by line according to the user inputed dictionary|

| TODO Task # 8      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **3**   |
| User case         | not signed                                       |
| Create date       | 2021-10-30 |
| Creator           | Shutian Wang |
| Assign date       | 2021-10-30 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Compile python model to dll let C++/C# program load it|

| TODO Task # 9      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **3**   |
| User case         | not signed                                       |
| Create date       | 2021-11-02 |
| Creator           | Shutian Wang |
| Assign date       | 2021-11-02 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Implement basic UI, it must have a menu, must have two listbar, one show loaded excel content, one show databast content|

| TODO Task # 10      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **3**   |
| User case         | not signed                                       |
| Create date       | 2021-11-02 |
| Creator           | Shutian Wang |
| Assign date       | 2021-11-02 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Implement a Python method, read the excel content and pass it to the UI part|

| TODO Task # 11      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **3**   |
| User case         | not signed                                       |
| Create date       | 2021-11-02 |
| Creator           | Shutian Wang |
| Assign date       | 2021-11-02 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Implement a Python method, read the database content and pass it to the UI part|

| TODO Task # 12      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **3**   |
| User case         | not signed                                       |
| Create date       | 2021-11-02 |
| Creator           | Shutian Wang |
| Assign date       | 2021-11-02 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Implement a function, read the excel data transfered from Python, update the UI, then delete the temporary file|

| TODO Task # 13      |                                                              |
| ----------------- | ------------------------------------------------------------ |
| Iteration         | **3**   |
| User case         | not signed                                       |
| Create date       | 2021-11-02 |
| Creator           | Shutian Wang |
| Assign date       | 2021-11-02 |
| Assignee          | Shutian Wang|
| Status            | Open|
| Task              | Implement a function, read the database data transfered from Python then delete the temporary file|