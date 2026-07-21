# Data structure of project

## **Entities**

Entities need to manage:

*   User
*   CV
*   JD
*   Analysis

## **Detail of entity:**

### **User**

*   userId
*   username
*   password
*   creatAt

### **CV**

*   cvId
*   userId
*   cvName
*   type (file or manual)
*   fileLink
*   content
*   createAt

### **JD**

*   jdId
*   jdName
*   type (file or manual)
*   fileLink
*   content
*   creatAt

### **Analysis**

*   id
*   user\_id
*   cv\_id
*   jd\_id
*   match\_score
*   result\_json
*   created\_at