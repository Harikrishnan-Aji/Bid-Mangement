create table  vendor(Vendor_ID int primary key,Vendor_Name varchar(50),
						Experience int,Demo varchar(100),Skills varchar(50),
						Course_ID varchar(20) foreign key references course(Course_ID)
						);
drop table vendor;
create table course(Course_ID varchar(20) primary key,Course_Name varchar(50),
					Levels varchar(25),Course_Description varchar(max),
					Training_Mode varchar(20)
					);
drop table course;

create table approver(Vendor_ID int foreign key references vendor(Vendor_ID),Vendor_Name varchar(50),
					  Experience int,Demo varchar(100),Duration time,Cost int,Bid_Status Varchar(50)
					  );
drop table approver;

create table bid(Bid_ID varchar(25) primary key,Bid_Duration time,min_Amount int,
					max_Amount int,Bidding_History varchar(100),Current_Bid_Amount int,
					Course_ID varchar(20) foreign key references course(Course_ID)
					);

