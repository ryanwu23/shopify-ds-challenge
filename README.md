# shopify-ds-challenge

## Question 1: Given some sample data, write a program to answer the following: click here to access the required data set

### On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

####  Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

This calculation is high because there are outliers that are pulling up the average value. A better way of evaulating this data is too use a metric that mitigates the impact of the those high order value outliers.

#### What metric would you report for this dataset?

The metric I would use is finding the median order value instead of the average order value.

#### What is its value?

The median order value is $284, which is much more reasonable.


## Question 2: For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

#### How many orders were shipped by Speedy Express in total?

54 orders were shipped by Speedy Express.

SQL Query Used:
`SELECT count(*) as "Orders Shipped by Speedy Express" FROM [Orders] where ShipperID = 1`

#### What is the last name of the employee with the most orders?

Peacock is the last name of the employee with the most orders.

SQL Query Used:
`SELECT Employees.LastName, count(*) as "Number of Orders" FROM [Orders] join [Employees] on Orders.EmployeeId = Employees.EmployeeId Group by Employees.LastName Order by "Number of Orders" DESC`

#### What product was ordered the most by customers in Germany?

Gorgonzola Telino was the product most ordered by customers in Germany.

SQL Query Used:
`SELECT Products.ProductName, COUNT(*) as NumOfOrders FROM [OrderDetails] JOIN [Orders] ON OrderDetails.OrderID = Orders.OrderID
JOIN [Customers] ON Customers.CustomerID = Orders.CustomerID AND Customers.Country = "Germany"
JOIN [Products] ON OrderDetails.ProductID = Products.ProductID
GROUP BY Products.ProductID
ORDER BY NumOfOrders DESC`
