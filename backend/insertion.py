import sqlite3

con = sqlite3.connect('trip_plannerr1.db')
cur = con.cursor()

cur.execute("""
INSERT INTO Trip (TripID, TripName, RecommendedStartMonth, RecommendedEndMonth, Description, Budget) VALUES

('IN_1', 'Exploring Taj Mahal', 'OCTOBER', 'OCTOBER','Experience the timeless beauty of Taj Mahal and the grandeur of India. October is the best time to visit Agra, as the weather is pleasant and sunny', 25000),

('US_1', 'Grand Canyon Adventure', 'APRIL', 'MAY', 'Embark on a thrilling adventure to the Grand Canyon, one of the natural wonders of the world. April to May is the ideal time to visit the Grand Canyon, as the temperatures are mild and the crowds are smaller', 30000),

('FR_1', 'Tour de Eiffel and Wine Country', 'MAY', 'JUNE', 'Immerse yourself in the romance of Paris and indulge in the finest wines of France. May and June are prime months to visit Paris, as the weather is warm and sunny, and the vineyards in wine country are in full bloom', 40000),

('IT_1', 'Colosseum and Vatican City', 'MARCH', 'MAY', 'Step back in time to explore the ancient ruins of Rome and witness the grandeur of Vatican City. Spring is the best time to visit Rome, as the weather is pleasant and there are fewer crowds', 25000),

('UK_1', 'Buckingham Palace and Stonehenge', 'JUNE', 'JULY', 'Experience the rich history and traditions of England, from the grandeur of Buckingham Palace to the mystery of Stonehenge. June and July are considered the peak season for visiting London, but that also means more crowds. Stonehenge is best visited during the summer solstice to witness the sun aligning with the stones.', 30000),

('NZ_1', 'Milford Sound and Fiordland National Park', 'OCTOBER', 'NOVEMBER', "Discover the breathtaking beauty of New Zealand's South Island, from the majestic Milford Sound to the pristine Fiordland National Park. Spring and autumn are the best times to visit New Zealand, as the weather is mild and the crowds are smaller", 40000),

('JP_1', 'Mount Fuji and Tokyo', 'APRIL', 'MAY', 'Experience the cultural wonders of Japan, from the iconic Mount Fuji to the vibrant city of Tokyo. April and May are the most popular times to visit Japan, as the cherry blossoms are in bloom. Spring is also an excellent time to visit Mount Fuji, as the weather is clear and the snow has melted.', 35000),

('AU_1', 'Sydney Harbour Bridge and Great Barrier Reef', 'NOVEMBER', 'DECEMBER', 'Explore the iconic landmarks of Australia, from the Sydney Harbour Bridge to the world-famous Great Barrier Reef. November to December is the best time to visit Sydney, as the weather is warm and sunny. The Great Barrier Reef can be visited year-round, but the best time to go is during the summer months', 45000),

('CA_1', 'Golden Gate Bridge and Yosemite National Park', 'MAY', 'JUNE', 'Uncover the natural beauty of California, from the iconic Golden Gate Bridge to the awe-inspiring Yosemite National Park. Spring and autumn are the best times to visit California, as the weather is mild and the crowds are smaller. Yosemite National Park is best visited during the spring or fall, when the waterfalls are flowing', 35000),

('BR_1', 'Christ the Redeemer and Amazon Rainforest', 'AUGUST', 'SEPTEMBER', 'Experience the wonders of Brazil, from the iconic Christ the Redeemer statue to the vast Amazon Rainforest. August to September is the best time to visit Brazil, as the weather is warm and dry', 40000)
""")

cur.execute("""
INSERT INTO Destination (TripID, DestinationID, Name, Country, City, Description) VALUES
('IN_1', 'IN_AG_1', 'Taj Mahal', 'India', 'Agra', 'An iconic white marble mausoleum, the Taj Mahal is a UNESCO World Heritage Site and one of the most recognizable landmarks in the world. Built by Mughal Emperor Shah Jahan in memory of his beloved wife Mumtaz Mahal, the Taj Mahals intricate architecture, delicate carvings, and serene gardens make it a masterpiece of Mughal art and a testament to eternal love'),
('IN_1', 'IN_AG_2', 'Agra Fort', 'India', 'Agra', 'A UNESCO World Heritage Site, Agra Fort is a 16th-century Mughal fort that served as the primary residence of the Mughal emperors until 1678. Its iconic red sandstone walls and white marble pavilions showcase the architectural brilliance of the Mughal era. The forts intricate carvings, grand courtyards, and beautifully landscaped gardens make it a must-visit destination for anyone exploring Indias rich heritage'),
('IN_1', 'IN_AG_3', 'Mehtab Bagh', 'India', 'Agra', 'Mehtab Bagh, also known as the Moonlight Garden, is a Mughal-era garden complex located across the Yamuna River from the Taj Mahal. Originally constructed in the 16th century by Emperor Akbar, Mehtab Bagh served as a pleasure garden for the Mughal emperors and their families. Today, it offers serene surroundings and breathtaking views of the Taj Mahal, making it a popular spot for photography and relaxation'),
('IN_1', 'IN_AG_4', 'Jama Masjid', 'India', 'Agra', 'Jama Masjid is a 17th-century mosque located in the heart of Agra. Built by Mughal Emperor Shah Jahan, the mosque is renowned for its red sandstone and white marble architecture, reminiscent of the Taj Mahal. Its spacious courtyard can accommodate up to 25,000 worshippers, making it one of the largest mosques in India. The mosques intricate carvings, towering minarets, and serene atmosphere make it a significant religious and cultural landmark in Agra'),
            
('US_1', 'US_GC_1', 'Grand Canyon National Park', 'USA', 'Arizona', 'A UNESCO World Heritage Site and one of the Seven Natural Wonders of the World, the Grand Canyon is a vast natural wonder that has captivated visitors for centuries. Carved over millions of years by the Colorado River, the canyons layers of rock reveal a rich geological history and offer breathtaking views of colorful cliffs, deep gorges, and diverse plant life. Hiking, mule rides, and helicopter tours provide unique perspectives on the canyons grandeur, while stargazing under the vast desert sky offers an unforgettable experience'),
('US_1', 'US_GC_01', 'South Rim', 'USA', 'Arizona', 'The most popular rim of the canyon, the South Rim offers stunning views of the canyons vast expanse and colorful rock layers. Its home to Grand Canyon Village, a hub of visitor services, restaurants, and hotels'),
('US_1', 'US_GC_02', 'North Rim', 'USA', 'Arizona', 'Less crowded and more secluded than the South Rim, the North Rim provides a different perspective of the canyon, with fewer developed areas and more opportunities for wildlife viewing'),
('US_1', 'US_GC_03', 'Desert View Watchtower', 'USA', 'Arizona', 'Perched atop a butte near the East Entrance, the Desert View Watchtower offers panoramic views of the canyon, including the Painted Desert and the Colorado River'),
('US_1', 'US_GC_04', 'Phantom Ranch', 'USA', 'Arizona', 'A secluded oasis nestled at the bottom of the canyon, Phantom Ranch is accessible by mule ride or hiking. Its a popular spot for overnight stays and offers a variety of activities, including hiking, rafting, and mule rides'),
            
('FR_1', 'FR_ET_01', 'Eiffel Tower', 'France', 'Paris', 'The iconic wrought-iron lattice tower is the tallest structure in Paris and one of the most recognizable landmarks in the world. Visitors can ascend to the top for panoramic views of the city'),
('FR_1', 'FR_ET_02', 'Champ de Mars', 'France', 'Paris', 'The sprawling park surrounding the Eiffel Tower is a popular spot for picnicking, sunbathing, and enjoying the views. Its also home to the Arc de Triomphe, a triumphal arch commemorating French military victories'),
('FR_1', 'FR_ET_03', 'Musée du Louvre', 'France', 'Paris', 'One of the worlds largest and most famous museums, the Louvre houses a vast collection of art, including Leonardo da Vincis Mona Lisa'),
('FR_1', 'FR_ET_04', 'Notre Dame Cathedral', 'France', 'Paris', 'A historic Gothic cathedral known for its stained glass windows and architectural beauty'),
('FR_1', 'FR_ET_05', 'Palace of Versailles', 'France', 'Versailles', 'A former royal residence located outside of Paris, the Palace of Versailles is known for its opulent architecture, lavish gardens, and grand fountains'),
            
('JP_1', 'JP_MT_01', 'Mount Fuji', 'Japan', 'Fujinomiya', 'An active volcano and Japans highest mountain, Mount Fuji is a revered symbol of beauty and tranquility. Visitors can hike to the summit or enjoy the views from lower elevations'),
('JP_1', 'JP_TK_01', 'Shibuya Crossing', 'Japan', 'Tokyo', 'One of the busiest pedestrian crossings in the world, Shibuya Crossing is a mesmerizing spectacle of synchronized movement and urban energy'),
('JP_1', 'JP_TK_02', 'Sensō-ji Temple', 'Japan', 'Tokyo', 'Tokyos oldest temple, Sensō-ji is a vibrant center of Buddhist worship and traditional culture'),
('JP_1', 'JP_TK_03', 'Tokyo Skytree', 'Japan', 'Tokyo', 'The tallest structure in Japan, the Tokyo Skytree offers panoramic views of the city and a glimpse into its futuristic skyline');
""")

cur.execute("""
INSERT INTO Accomodation (TripID, AccomodationID, Name, Type, Location, Cost) VALUES
('IN_1', 'IN_1_AG', 'Taj Mahal Palace', 'Hotel', 'Agra, India', 5000),
('US_1', 'US_1_GC', 'El Tovar Hotel', 'Hotel', 'Grand Canyon National Park, USA', 3000),
('FR_1', 'FR_1_ET', 'Hotel Plaza Athénée', 'Hotel', 'Paris, France', 6000),
('IT_1', 'IT_1_CV', 'Hotel Raphael', 'Hotel', 'Rome, Italy', 4500)
""")

cur.execute("""
INSERT INTO Transportation (TransportID, Mode, DepartureDatetime, ArrivalDatetime, DepartureLocation, ArrivalLocation, Cost) VALUES
('IN_1_FT', 'Flight', '2023-12-19 10:00:00', '2023-12-19 14:00:00', 'New York, USA', 'Delhi, India', 100000),
('US_1_FL', 'Flight', '2024-01-09 18:00:00', '2024-01-09 22:00:00', 'Los Angeles, USA', 'Phoenix, USA', 80000),
('FR_1_TR', 'Train', '2024-02-14 16:00:00', '2024-02-14 20:00:00', 'London, UK', 'Paris, France', 40000),
('IT_1_FL', 'Flight', '2024-03-04 12:00:00', '2024-03-04 14:00:00', 'New York, USA', 'Rome, Italy', 120000),
('UK_1_TR', 'Train', '2024-04-19 10:00:00', '2024-04-19 12:00:00', 'London, UK', 'Edinburgh, UK', 20000),
('NZ_1_FL', 'Flight', '2024-05-14 08:00:00', '2024-05-14 16:00:00', 'Los Angeles, USA', 'Auckland, New Zealand', 200000),
('JP_1_FL', 'Flight', '2024-06-04 20:00:00', '2024-06-05 08:00:00', 'New York, USA', 'Tokyo, Japan', 180000),
('AU_1_FL', 'Flight', '2024-07-19 22:00:00', '2024-07-20 06:00:00', 'Los Angeles, USA', 'Sydney, Australia', 250000),
('CA_1_FL', 'Flight', '2024-08-14 14:00:00', '2024-08-14 18:00:00', 'New York, USA', 'San Francisco, USA', 100000),
('BR_1_FL', 'Flight', '2024-09-04 16:00:00', '2024-09-04 22:00:00', 'Miami, USA', 'Rio de Janeiro, Brazil', 150000)
""")

cur.execute("""
INSERT INTO Recommendation (RecommendationID, Type, Name, Description, Rating) VALUES
('IN_1_RC1', 'Restaurant', 'Agrasen Ki Baoli', 'A historic stepwell with a charming restaurant serving traditional Indian cuisine.', 4.5),
('US_1_RC1', 'Hike', 'South Kaibab Trail', 'A scenic hike that offers stunning views of the Grand Canyon.', 5),
('FR_1_RC1', 'Museum', 'Louvre Museum', 'One of the worlds largest and most renowned museums, housing a vast collection of art and artifacts.', 5),
('IT_1_RC1', 'Restaurant', 'La Pergola', 'A Michelin-starred restaurant known for its innovative and exquisite Italian cuisine.', 5),
('UK_1_RC1', 'Castle', 'Windsor Castle', 'A historic castle that has been the home of British monarchs for over 900 years.', 5),
('NZ_1_RC1', 'Boat Tour', 'Milford Sound Cruise', 'A breathtaking boat tour through the fiords of Milford Sound.', 5),
('JP_1_RC1', 'Onsen', 'Dōgo Onsen', 'One of the oldest and most famous hot springs in Japan.', 5)
""")

cur.execute("""
INSERT INTO Activity (ActivityID, Name, Description, Date, Time, Cost)
VALUES ('US_NYC_1', 'Visit the Empire State Building', 'Enjoy breathtaking views of New York City from the top of the Empire State Building.', '2023-11-15', '10:00:00', 35.00),
('US_LA_2', 'Explore Disneyland Park', 'Immerse yourself in the magic of Disneyland Park, where dreams come true.', '2023-11-16', '09:00:00', 95.00),
('CA_TOR_3', 'Hike to the top of CN Tower', 'Challenge yourself with a scenic hike to the top of the iconic CN Tower.', '2023-11-17', '12:00:00', 25.00),
('FR_PAR_4', 'Cruise along the Seine River', 'Experience the romance of Paris with a leisurely cruise along the Seine River.', '2023-11-18', '16:00:00', 40.00),
('IT_ROM_5', 'Visit the Colosseum and Roman Forum', 'Step back in time and explore the ancient wonders of the Colosseum and Roman Forum.', '2023-11-19', '14:00:00', 20.00);
""")

cur.execute("""
INSERT INTO Weather (WeatherID, Date, Temp, Conditions)
VALUES ('US_NYC_1', '2023-11-15', 55, 'Partly cloudy'),
('US_LA_2', '2023-11-16', 72, 'Sunny'),
('CA_TOR_3', '2023-11-17', 58, 'Scattered showers'),
('FR_PAR_4', '2023-11-18', 45, 'Overcast'),
('IT_ROM_5', '2023-11-19', 63, 'Mostly sunny');
""")


con.commit()
print("done")