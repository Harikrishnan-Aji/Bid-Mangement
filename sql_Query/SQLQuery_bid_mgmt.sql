create table vendor(Title varchar(255),Vendor_ID int primary key,Vendor_Name varchar(50),Duration int,Experience int,Expected_Cost int,Demo varchar(max),Skills varchar(50),Description varchar(max));


--create table approver(Title varchar(255),Vendor_ID int primary key,Vendor_Name varchar(50),Duration int,Experience int,Expected_Cost int,Demo varchar(max),Skills varchar(50),Description varchar(max),);


create table course(course_id int primary key,c_title varchar(255),c_description varchar(max),image_url varchar(max));
insert into course values(1,'Advanced Python','This Python training course leads students from the basics writing and running Python scripts to more advanced features such as file operations,regular expressions, working with binary data, and using the extensive functionality of Python modules. Extra emphasis is placed on features unique to Python, such as tuples, array slices, and output formatting.','https://cdn.devdojo.com/posts/images/March2021/python-app-development-what-can-you-build-with-python.jpg?auto=format&q=70&w=1280')
insert into course values(2,'Javascript','JavaScript is among the most powerful and flexible programming languages of the web. It powers the dynamic behavior on most websites, including this one.You will learn programming fundamentals and basic object-oriented concepts using the latest JavaScript syntax. The concepts covered in these lessons lay the foundation for using JavaScript in any environment.','https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/768px-Unofficial_JavaScript_logo_2.svg.png?20141107110902')
insert into course values(3,'Devops Cloud','A Professional Cloud DevOps Engineer is responsible for efficient development operations that can balance service reliability and delivery speed. They are skilled at using Google Cloud to build software delivery pipelines, deploy and monitor services, and manage and learn from incidents.The Professional Cloud DevOps Engineer exam assesses your ability','https://imageio.forbes.com/specials-images/imageserve/60f1e792c7e89f933811814c/DevOps-concept/960x0.jpg?format=jpg&width=960')
insert into course values(4,'Advanced Excel','Enroll now to go through a deep dive of the most popular spreadsheet tool on the market, Microsoft Excel. As a Microsoft Certified Trainer I will use my 20+ years of Excel training to guide you step by step through the beginner to advanced level and beyond.As you participate in each of the 4 courses you will master Excel tools that will clear away.','https://sharmacomputers.net/wp-content/uploads/2022/02/advanced_excel.jpg')
insert into course values(5,'Cloud Computing','The Cloud Architect Certification program is designed to make you an expert in cloud applications and architecture. It will enable you to master the core skillsets required for designing and deploying dynamically scalable, highly available, fault-tolerant, and reliable applications on three of the top Cloud platform providers � AWS, Microsoft Azure- etc.','https://s40424.pcdn.co/in/wp-content/uploads/2022/07/cloud-computing.jpg')
insert into course values(6,'HTML & CSS','HTML & CSS makes it easier for you to learn other coding languages if you are thinking to become a web developer. HTML & CSS are the frameworks used to build websites. No expertisation is necessary if you understand how they can work together you�re much better off when it comes to design, marketing, and several other professions. There are several coding languages.','https://www.sithub.in/html-css/images/html-css.png')

select * from course





