import classes_exo_package.products as products

instance_product = products.Product(1000,1000,"toto")
instance_Furniture = products.Furniture(1000,1000,"toto","wood","green",(150,100,100))
instance_Chair = products.Chair(1000,1000,"toto","wood","green",(150,100,100))
instance_Couch = products.Couch(1000,1000,"toto","wood","green",(150,100,100))
instance_Table = products.Table(1000,1000,"toto","wood","green",(150,100,100))

canape1 = products.Couch(1000,2000,"OKLM","Cuir","Blanc", (200,100,80))
canape2 = products.Couch(800,1600,"SIESTA","TISSU","Bleu", (150,90,70))

chaise1 = products.Chair(50,100,"PEPOUSE","Plastique","Rouge",(50,50,70))
chaise2 = products.Chair(75,150,"PEPOUSE","Metal","Gris",(60,60,80))

table1 = products.Table(250,500,"TEX","Bois","Chêne",(150,80,75))
table2 = products.Table(350,700,"TEX","Verre","Transparent",(120,60,75))

print(vars(table2))