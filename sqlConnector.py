from sqlalchemy import create_engine
db = create_engine('sqlite:///webshopDB.sqlite')

# ispis u konzoli
db.echo = True
conn = db.connect() 
# Otvaramo transakciju

 
#punjenje kategorija

conn.execute("INSERT INTO 'category' (id, name) VALUES (1, 'Jednobojne narukvice');")
conn.execute("INSERT INTO 'category' (id, name) VALUES (2, 'Visebojne narukvice');")
conn.execute("INSERT INTO 'category' (id, name) VALUES (3, 'Narukvice s natpisima');")
conn.execute("INSERT INTO 'category' (id, name) VALUES (4, 'Narukvice s privjescima');")
conn.execute("INSERT INTO 'category' (id, name) VALUES (5, 'Setovi');")

#punjenje proizvoda/ kategorija 5 - setovi
conn.execute("INSERT INTO product VALUES (1, 'set_baby_pink_gold', 'Set Baby Pink', 5, 120, 'static/images/set_baby_pink_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (2, 'set_baby_blue_gold','Set Baby Blue', 5, 120, 'static/images/set_baby_blue_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (3, 'set_beige_gold', 'Set Beige Gold', 5, 120, 'static/images/set_beige_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (4, 'set_bondi_blue_gold', 'Set Bondi Blue', 5, 120, 'static/images/set_bondi_blue_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (5, 'set_brown_gold', 'Set Brown Gold', 5, 120, 'static/images/set_brown_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (6, 'set_deep_yellow_gold', 'Set Yellow Gold', 5, 120, 'static/images/set_deep_yellow_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (7, 'set_denim_blue_gold', 'Set Blue Gold', 5, 120, 'static/images/set_denim_blue_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (8, 'set_fuchsija_gold', 'Set Fuchsija Gold', 5, 120, 'static/images/set_fuchsija_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (9, 'set_gold_yellow_gold', 'Set Gold Yellow Gold', 5, 120, 'static/images/set_gold_yellow_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (10, 'set_king_blue_gold', 'Set King Blue Gold', 5, 120, 'static/images/set_king_blue_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (11, 'set_limete_gold', 'Set Limette Gold', 5, 120, 'static/images/set_limete_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (12, 'set_mint_gold', 'Set Mint Gold', 5, 120, 'static/images/set_mint_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (13, 'set_ocher_yellow_gold', 'Set Ocher Yellow Gold', 5, 120, 'static/images/set_ocher_yellow_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (14, 'set_orange_gold', 'Set Orange Gold', 5, 120, 'static/images/set_orange_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (15, 'set_pastel_yellow_gold', 'Set Pastel Yellow Gold', 5, 120, 'static/images/set_pastel_yellow.jpg' );")
conn.execute("INSERT INTO product VALUES (16, 'set_peachy_gold', 'Set Peachy Gold', 5, 120, 'static/images/set_peachy_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (17, 'set_pink_brown_gold', 'Set Pink Brown Gold', 5, 120, 'static/images/set_pink_brown_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (18, 'set_pink_gold', 'Set Pink Gold', 5, 120, 'static/images/set_pink_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (19, 'set_pink_peach_gold', 'Set Pink Peach Gold', 5, 120, 'static/images/set_pink_peach_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (20, 'set_powder_gold', 'Set Powder Gold', 5, 120, 'static/images/set_powder_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (21, 'set_tiffany_blue_gold', 'Set Tiffany Gold', 5, 120, 'static/images/set_tiffany_blue_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (22, 'set_white_gold', 'Set White Gold', 5, 120, 'static/images/set_white_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (23, 'set_mint_green_gold', 'Set Mint Green Gold', 5, 120, 'static/images/set_mint_green_gold.jpg' );")
conn.execute("INSERT INTO product VALUES (24, 'set_coral_gold', 'Set Coral Gold', 5, 120, 'static/images/set_coral_gold.jpg' );")


#jednobojne - 1

conn.execute("INSERT INTO product VALUES (25, 'jed_1_1', 'Green Thin Waves', 1, 30, 'static/images/jed_1_1.jpg' );")
conn.execute("INSERT INTO product VALUES (26, 'jed_2_1', 'Rose Thin Waves', 1, 30, 'static/images/jed_2_1.jpg' );")
conn.execute("INSERT INTO product VALUES (27, 'jed_3_1', 'Peach Thin Waves', 1, 30, 'static/images/jed_3_1.jpg' );")
conn.execute("INSERT INTO product VALUES (28, 'jed_4_1', 'Orange Thin Waves', 1, 30, 'static/images/jed_4_1.jpg' );")
conn.execute("INSERT INTO product VALUES (29, 'jed_5_1', 'Powder Thin Waves', 1, 30, 'static/images/jed_5_1.jpg' );")
conn.execute("INSERT INTO product VALUES (30, 'jed_6_1', 'Blue Thin Waves', 1, 30, 'static/images/jed_6_1.jpg' );")
conn.execute("INSERT INTO product VALUES (31, 'jed_7_1', 'Emerald Thin Waves', 1, 30, 'static/images/jed_7_1.jpg' );")
conn.execute("INSERT INTO product VALUES (32, 'jed_8_1', 'King Thin Waves', 1, 30, 'static/images/jed_8_1.jpg' );")
conn.execute("INSERT INTO product VALUES (33, 'jed_9_1', 'Mint Thin Waves', 1, 30, 'static/images/jed_9_1.jpg' );")
conn.execute("INSERT INTO product VALUES (34, 'jed_10_1', 'Yellow Thin Waves', 1, 30, 'static/images/jed_10_1.jpg' );")
conn.execute("INSERT INTO product VALUES (35, 'jed_11_1', 'Pink Thin Waves', 1, 30, 'static/images/jed_11_1.jpg' );")
conn.execute("INSERT INTO product VALUES (36, 'jed_12_1', 'Oragne Waves', 1, 30, 'static/images/jed_12_1.jpg' );")
conn.execute("INSERT INTO product VALUES (37, 'jed_13_1', 'Grey Waves', 1, 30, 'static/images/jed_13_1.jpg' );")
conn.execute("INSERT INTO product VALUES (38, 'jed_14_1', 'Dark Pink Waves', 1, 30, 'static/images/jed_14_1.jpg' );")
conn.execute("INSERT INTO product VALUES (39, 'jed_15_1', 'Light Pink Waves', 1, 30, 'static/images/jed_15_1.jpg' );")
conn.execute("INSERT INTO product VALUES (40, 'jed_16_1', 'Light Olive Waves', 1, 30, 'static/images/jed_16_1.jpg' );")
conn.execute("INSERT INTO product VALUES (41, 'jed_17_1', 'Blue King Waves', 1, 30, 'static/images/jed_17_1.jpg' );")
conn.execute("INSERT INTO product VALUES (42, 'jed_18_1', 'Yellow Waves', 1, 30, 'static/images/jed_18_1.jpg' );")
conn.execute("INSERT INTO product VALUES (43, 'jed_19_1', 'Limete Waves', 1, 30, 'static/images/jed_19_1.jpg' );")
conn.execute("INSERT INTO product VALUES (44, 'jed_20_1', 'Olive Waves', 1, 30, 'static/images/jed_20_1.jpg' );")
conn.execute("INSERT INTO product VALUES (45, 'jed_21_1', 'Rosy Waves', 1, 30, 'static/images/jed_21_1.jpg' );")
conn.execute("INSERT INTO product VALUES (46, 'jed_22_1', 'Powder Waves', 1, 30, 'static/images/jed_22_1.jpg' );")
conn.execute("INSERT INTO product VALUES (47, 'jed_23_1', 'Bondi Waves', 1, 30, 'static/images/jed_23_1.jpg' );")
conn.execute("INSERT INTO product VALUES (48, 'jed_24_1', 'Emerald Waves', 1, 30, 'static/images/jed_24_1.jpg' );")
conn.execute("INSERT INTO product VALUES (49, 'jed_25_1', 'White Waves', 1, 30, 'static/images/jed_25_1.jpg' );")
conn.execute("INSERT INTO product VALUES (50, 'jed_26_1', 'King Waves', 1, 30, 'static/images/jed_26_1.jpg' );")
conn.execute("INSERT INTO product VALUES (51, 'jed_27_1', 'Coral Thin Waves', 1, 30, 'static/images/jed_27_1.jpg' );")

#natpisi-3
conn.execute("INSERT INTO product VALUES (52, 'cool', 'Cool', 3, 90, 'static/images/cool.jpg' );")
conn.execute("INSERT INTO product VALUES (53, 'feel', 'Feel', 3, 90, 'static/images/feel.jpg' );")
conn.execute("INSERT INTO product VALUES (54, 'free', 'Free', 3, 90, 'static/images/free.jpg' );")
conn.execute("INSERT INTO product VALUES (55, 'happy', 'Happy', 3, 90, 'static/images/happy.jpg' );")
conn.execute("INSERT INTO product VALUES (56, 'honest', 'Honest', 3, 90, 'static/images/honest.jpg' );")
conn.execute("INSERT INTO product VALUES (57, 'hope', 'Hope', 3, 90, 'static/images/hope.jpg' );")
conn.execute("INSERT INTO product VALUES (58, 'joy', 'Joy', 3, 90, 'static/images/joy.jpg' );")
conn.execute("INSERT INTO product VALUES (59, 'life', 'Life', 3, 90, 'static/images/life.jpg' );")
conn.execute("INSERT INTO product VALUES (60, 'smile', 'Smile', 3, 90, 'static/images/smile.jpg' );")
conn.execute("INSERT INTO product VALUES (61, 'summer', 'Summer', 3, 90, 'static/images/summer.jpg' );")
conn.execute("INSERT INTO product VALUES (62, 'sun', 'Sun', 3, 90, 'static/images/sun.jpg' );")
conn.execute("INSERT INTO product VALUES (63, 'sweet', 'Sweet', 3, 90, 'static/images/sweet.jpg' );")

#višebojne-2
conn.execute("INSERT INTO product VALUES (64, 'vi_1', 'Peach', 2, 70, 'static/images/vi_1.jpg' );")
conn.execute("INSERT INTO product VALUES (65, 'vi_2', 'Coconut', 2, 70, 'static/images/vi_2.jpg' );")
conn.execute("INSERT INTO product VALUES (66, 'vi_3', 'Rose', 2, 70, 'static/images/vi_3.jpg' );")
conn.execute("INSERT INTO product VALUES (67, 'vi_4', 'Rainbow', 2, 70, 'static/images/vi_4.jpg' );")
conn.execute("INSERT INTO product VALUES (68, 'vi_5', 'Yellow eye', 2, 70, 'static/images/vi_5.jpg' );")
conn.execute("INSERT INTO product VALUES (69, 'vi_6', 'Candy', 2, 70, 'static/images/vi_6.jpg' );")
conn.execute("INSERT INTO product VALUES (70, 'vi_7', 'Sea', 2, 70, 'static/images/vi_7.jpg' );")
conn.execute("INSERT INTO product VALUES (71, 'vi_8', 'Boho', 2, 70, 'static/images/vi_8.jpg' );")
conn.execute("INSERT INTO product VALUES (72, 'vi_9', 'Fruty', 2, 70, 'static/images/vi_9.jpg' );")
conn.execute("INSERT INTO product VALUES (73, 'vi_10', 'Azzure', 2, 70, 'static/images/vi_10.jpg' );")
conn.execute("INSERT INTO product VALUES (74, 'vi_11', 'Classy', 2, 70, 'static/images/vi_11.jpg' );")
conn.execute("INSERT INTO product VALUES (75, 'vi_12', 'Deep Sea', 2, 70, 'static/images/vi_12.jpg' );")
conn.execute("INSERT INTO product VALUES (76, 'vi_13', 'Pastel Wave', 2, 70, 'static/images/vi_13.jpg' );")
conn.execute("INSERT INTO product VALUES (77, 'vi_14', 'Royal', 2, 70, 'static/images/vi_14.jpg' );")
conn.execute("INSERT INTO product VALUES (78, 'vi_15', 'Anchor', 2, 70, 'static/images/vi_15.jpg' );")
conn.execute("INSERT INTO product VALUES (79, 'vi_16', 'Salt', 2, 70, 'static/images/vi_16.jpg' );")
conn.execute("INSERT INTO product VALUES (80, 'vi_17', 'Magic', 2, 70, 'static/images/vi_17.jpg' );")
conn.execute("INSERT INTO product VALUES (81, 'vi_18', 'Gold Shade', 2, 70, 'static/images/vi_18.jpg' );")
conn.execute("INSERT INTO product VALUES (82, 'vi_19', 'Summer Shine', 2, 70, 'static/images/vi_19.jpg' );")
conn.execute("INSERT INTO product VALUES (83, 'vi_20', 'Paradise', 2, 70, 'static/images/vi_20.jpg' );")
conn.execute("INSERT INTO product VALUES (84, 'vi_21', 'Sparkly', 2, 70, 'static/images/vi_21.jpg' );")
conn.execute("INSERT INTO product VALUES (85, 'vi_22', 'Beige Spark', 2, 70, 'static/images/vi_22.jpg' );")
conn.execute("INSERT INTO product VALUES (86, 'vi_23', 'Natural', 2, 70, 'static/images/vi_23.jpg' );")
conn.execute("INSERT INTO product VALUES (87, 'vi_24', 'Burgundy Shade', 2, 70, 'static/images/vi_24.jpg' );")
conn.execute("INSERT INTO product VALUES (88, 'vi_25', 'Beige Gold', 2, 70, 'static/images/vi_25.jpg' );")
conn.execute("INSERT INTO product VALUES (89, 'vi_26', 'Sunflower', 2, 70, 'static/images/vi_26.jpg' );")
conn.execute("INSERT INTO product VALUES (90, 'vi_27', 'Candy Gold', 2, 70, 'static/images/vi_27.jpg' );")
conn.execute("INSERT INTO product VALUES (91, 'vi_28', 'Minty', 2, 70, 'static/images/vi_28.jpg' );")
conn.execute("INSERT INTO product VALUES (92, 'vi_29', 'Peachy', 2, 70, 'static/images/vi_29.jpg' );")
conn.execute("INSERT INTO product VALUES (93, 'vi_30', 'Fuchsia', 2, 80, 'static/images/vi_30.jpg' );")
conn.execute("INSERT INTO product VALUES (94, 'vi_31', 'Orange', 2, 80, 'static/images/vi_31.jpg' );")
conn.execute("INSERT INTO product VALUES (95, 'vi_32', 'Lime', 2, 80, 'static/images/vi_32.jpg' );")
conn.execute("INSERT INTO product VALUES (96, 'vi_33', 'Mentol', 2, 80, 'static/images/vi_33.jpg' );")
conn.execute("INSERT INTO product VALUES (97, 'vi_34', 'Pink Shade', 2, 80, 'static/images/vi_34.jpg' );")
conn.execute("INSERT INTO product VALUES (98, 'vi_35', 'Emerald', 2, 80, 'static/images/vi_35.jpg' );")
conn.execute("INSERT INTO product VALUES (99, 'vi_36', 'Browny', 2, 80, 'static/images/vi_36.jpg' );")
conn.execute("INSERT INTO product VALUES (100, 'vi_37', 'Brown Pinky', 2, 80, 'static/images/vi_37.jpg' );")
conn.execute("INSERT INTO product VALUES (101, 'vi_38', 'White Gold', 2, 80, 'static/images/vi_38.jpg' );")
conn.execute("INSERT INTO product VALUES (102, 'vi_39', 'Denim', 2, 80, 'static/images/vi_39.jpg' );")
conn.execute("INSERT INTO product VALUES (103, 'vi_40', 'Bondy', 2, 80, 'static/images/vi_40.jpg' );")
conn.execute("INSERT INTO product VALUES (104, 'vi_41', 'Petroleum Gold', 2, 80, 'static/images/vi_41.jpg' );")
conn.execute("INSERT INTO product VALUES (105, 'vi_42', 'Lilac Wave', 2, 80, 'static/images/vi_42.jpg' );")
conn.execute("INSERT INTO product VALUES (106, 'vi_43', 'Lilac Shade', 2, 80, 'static/images/vi_43.jpg' );")
conn.execute("INSERT INTO product VALUES (107, 'vi_44', 'Tiffany', 2, 80, 'static/images/vi_44.jpg' );")





conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (1, 25, 'static/images/jed_1_1.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (2, 25, 'static/images/jed_1_2.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (3, 26, 'static/images/jed_2_1.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (4, 26, 'static/images/jed_2_2.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (5, 27, 'static/images/jed_3_1.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (6, 27, 'static/images/jed_3_2.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (7, 28, 'static/images/jed_4_1.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (8, 28, 'static/images/jed_4_2.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (9, 29, 'static/images/jed_5_1.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (10, 29, 'static/images/jed_5_2.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (11, 30, 'static/images/jed_6_1.jpg');")
conn.execute("INSERT INTO 'product_image' (id, product_id, image) VALUES (12, 30, 'static/images/jed_6_2.jpg');")





 
# vratimo konekciju u "connection pool"
conn.close()