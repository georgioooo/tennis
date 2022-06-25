import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn.tree import DecisionTreeClassifier
from sklearn import ensemble
import streamlit as st

df1 = pd.read_csv("atp-2022.txt")
df2 = pd.read_csv("atp_2021.txt")
df3 = pd.read_csv("atp_2020.txt")
df4 = pd.read_csv("atp_2019.txt")
df5 = pd.read_csv("atp_2018.txt")
df6 = pd.read_csv("atp_2017.txt")
df7 = pd.read_csv("atp_2016.txt")
df8 = pd.read_csv("atp_2015.txt")
df9 = pd.read_csv("atp_2014.txt")
df10 = pd.read_csv("atp_2013.txt")
df11 = pd.read_csv("atp_2012.txt")
df12 = pd.read_csv("atp_2011.txt")
df13 = pd.read_csv("atp_2010.txt")

union = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13], axis=0)

new_df = union[['tourney_date', 'tourney_name', 'surface', 'round', 'tourney_level', 'winner_hand', 'loser_hand',
                'winner_rank', 'loser_rank', 'winner_ht', 'loser_ht', 'winner_age', 'loser_age', 'winner_name',
                'loser_name']]

new_df = new_df.sort_values('tourney_date', axis=0)

new_df.reset_index(drop=True, inplace=True)
df = new_df
df['winner_age'] = round(df['winner_age'])
df['loser_age'] = round(df['loser_age'])

col1, col2, col3 = st.columns(3)

with col1:
    first_player = st.selectbox('first player', sorted(['Radek Stepanek',
                                                        'Andy Roddick', 'Gael Monfils', 'Tomas Berdych',
                                                        'Wayne Odesnik', 'Thomaz Bellucci', 'Richard Gasquet',
                                                        'Alexandr Dolgopolov', 'James Blake', 'Alejandro Falla',
                                                        'Carsten Ball', 'Matthew Ebden', 'Marcos Baghdatis',
                                                        'Marc Gicquel', 'Florent Serra', 'Harel Levy', 'Lukasz Kubot',
                                                        'Potito Starace', 'Younes El Aynaoui', 'Steve Darcis',
                                                        'Sergiy Stakhovsky', 'Olivier Rochus', 'Ernests Gulbis',
                                                        'Ivo Karlovic', 'Benjamin Becker', 'Marco Chiudinelli',
                                                        'Nikolay Davydenko', 'Andreas Seppi', 'Rafael Nadal',
                                                        'Viktor Troicki', 'Roger Federer', 'Marin Cilic',
                                                        'Evgeny Korolev',
                                                        'Michael Berrer', 'Robby Ginepri', 'Lukas Lacko', 'Kevin Kim',
                                                        'Dudi Sela', 'Stan Wawrinka', 'Michael Russell',
                                                        'Stephane Robert',
                                                        'Thiemo De Bakker', 'Somdev Devvarman', 'Janko Tipsarevic',
                                                        'Jan Hajek', 'Santiago Giraldo', 'Robin Haase',
                                                        'Marcel Granollers', 'Peter Luczak', 'Mardy Fish',
                                                        'Leonardo Mayer', 'Pablo Cuevas', 'Julien Benneteau',
                                                        'Lleyton Hewitt', 'John Isner', 'Sebastien Grosjean',
                                                        'Arnaud Clement', 'Simon Greul', 'Juan Monaco',
                                                        'Michael Lammer',
                                                        'Jose Rubin Statham', 'Philipp Kohlschreiber', 'Jurgen Melzer',
                                                        'Albert Montanes', 'Tommy Robredo', 'Fernando Gonzalez',
                                                        'Florian Mayer', 'Andy Murray', 'Feliciano Lopez',
                                                        'Ivan Ljubicic',
                                                        'Juan Martin del Potro', 'Fernando Verdasco', 'Nicolas Almagro',
                                                        'Tommy Haas', 'Jo-Wilfried Tsonga', 'Mikhail Youzhny',
                                                        'Denis Istomin', 'Novak Djokovic', 'Stefan Koubek',
                                                        'Ivan Dodig',
                                                        'Taylor Dent', 'Michael Llodra', 'Ivan Sergeyev',
                                                        'David Ferrer',
                                                        'Donald Young', 'Victor Hanescu', 'Illya Marchenko',
                                                        'Andrey Golubev', 'Antonio Veic', 'Louk Sorensen',
                                                        'Jarkko Nieminen', 'Marsel Ilhan', 'Rainer Schuettler',
                                                        'Bernard Tomic', 'Igor Kunitsyn', 'Alexandre Sidorenko',
                                                        'Daniel Koellerer', 'Joao Souza', 'Eduardo Schwank',
                                                        'Alberto Martin', 'Philipp Petzschner', 'Mikhail Kukushkin',
                                                        'Petar Jelenic', 'Juan Ignacio Chela', 'Yen Hsun Lu',
                                                        'Filip Prpic', 'Thiago Alves', 'David Marrero',
                                                        'Laurent Recouderc', 'Izak Van Der Merwe', 'Rajeev Ram',
                                                        'Bjorn Phau', 'Blaz Kavcic', 'Raven Klaasen', 'Josselin Ouanna',
                                                        'Dustin Brown', 'Pere Riba', 'Jose Acasuso', 'Paul Capdeville',
                                                        'Ricardo Mello', 'Ruben Ramirez Hidalgo', 'Robin Soderling',
                                                        'Xavier Malisse', 'Sam Querrey', 'Ricardas Berankis',
                                                        'Juan Carlos Ferrero', 'Carlos Berlocq', 'Fabio Fognini',
                                                        'Igor Andreev', 'Rui Machado', 'Frederico Gil',
                                                        'Daniel Gimeno Traver', 'Nicolas Massu', 'Igor Sijsling',
                                                        'Mischa Zverev', 'Guillaume Rufin', 'Jeremy Chardy',
                                                        'David Nalbandian', 'Marcos Daniel', 'Santiago Ventura',
                                                        'Carlos Moya', 'Horacio Zeballos', 'Pablo Andujar',
                                                        'Yannick Mertens', 'Daniel Brands', 'Teymuraz Gabashvili',
                                                        'Ramon Delgado', 'Alexander Blom', 'Nicolas Salama',
                                                        'Ivan Miranda', 'Mauricio Echazu', 'Alvaro Raposo De Oliveira',
                                                        'Pedro Sousa', 'Martin Pedersen', 'Diego Galeano',
                                                        'Daniel King Turner', 'Sergio Galdos', 'Siu Fai Kelvin Lam',
                                                        'Aldin Setkic', 'Aisam Ul Haq Qureshi', 'Hiu Tung Yu',
                                                        'Aljaz Bedene', 'Luka Gregorc', 'Grega Zemlja', 'Ismar Gorcic',
                                                        'Predrag Rusevski', 'Cesar Ramirez', 'Bruno Rodriguez',
                                                        'Harshana Godamanna', 'Kittipong Wachiramanowong',
                                                        'Sunu Wahyu Trijati', 'Rohan Bopanna',
                                                        'Peerakiat Siriluethaiwattana', 'Lukas Dlouhy',
                                                        'David Agung Susanto', 'Conor Niland', 'Christopher Rungkat',
                                                        'Henri Kontinen', 'Go Soeda', 'Tatsuma Ito', 'Filippo Volandri',
                                                        'Simone Bolelli', 'Ariel Behar', 'Jhonson Garcia',
                                                        'Marcel Felder',
                                                        'Di Wu', 'Ze Zhang', 'Laurynas Grigelis', 'James Ward',
                                                        'Barry King', 'James Mcgee', 'Vladimir Ivanov', 'Jurgen Zopp',
                                                        'Adam Kellner', 'Sherif Sabry', 'Thomas Oger', 'Karim Maamoun',
                                                        'Carlos Salamanca', 'Juan Sebastian Cabal', 'Martin Klizan',
                                                        'Roman Recarte', 'Mauricio Doria Medina', 'Piero Luisi',
                                                        'Benjamin Balleret', 'Grigor Dimitrov', 'Yohny Romero',
                                                        'Jorge Aguilar', 'Brian Dabul', 'Guillermo Garcia Lopez',
                                                        'Mario Ancic', 'Paul Henri Mathieu', 'Marinko Matosevic',
                                                        'Kevin Anderson', 'Ryan Harrison', 'Nicolas Lapentti',
                                                        'Ryan Sweeting', 'Reda El Amrani', 'Oscar Hernandez',
                                                        'Ivan Navarro', 'Albert Ramos', 'Paolo Lorenzi', 'Andreas Beck',
                                                        'Leonardo Tavares', 'Filip Krajinovic', 'Alessio Di Mauro',
                                                        'Rik De Voest', 'Marcelo Melo', 'Daniel Munoz de la Nava',
                                                        'Julian Reister', 'Edouard Roger Vasselin', 'Tobias Kamke',
                                                        'Kei Nishikori', 'Yuri Schukin', 'Nicolas Mahut',
                                                        'Gilles Muller',
                                                        'Jesse Levine', 'Nicolas Kiefer', 'Dominik Meffert',
                                                        'Gilles Simon', 'Andrey Kuznetsov', 'Michal Przysiezny',
                                                        'Karol Beck', 'Brendan Evans', 'Ilija Bozoljac',
                                                        'Martin Fischer',
                                                        'Frank Dancevic', 'Richard Bloomfield', 'Sergei Bubka',
                                                        'Denis Kudla', 'Austen Childs', 'Joao Sousa', 'Daniel Garza',
                                                        'Daniel Alejandro Lopez Cassaccia', 'Weerapat Doakmaiklee',
                                                        'Blaz Rola', 'Damir Dzumhur', 'Ivo Minar', 'David Souto',
                                                        'Jamie Baker', 'Soren Wedege', 'Thomas Kromann',
                                                        'Frederik Nielsen', 'Hugo Dellien', 'Rodrigo Rappaccioli',
                                                        'Marcelo Arevalo', 'Rafael Arevalo', 'Hsin Han Lee',
                                                        'Tsung Hua Yang', 'Yong Kyu Lim', 'Hyun Joon Kim',
                                                        'Farrukh Dustov', 'Cecil Mamiit', 'Dineshkanthan Thangarajah',
                                                        'Martin Sayer', 'Abd Hazli Bin Zainuddin', 'Michael Leong',
                                                        'Yew Ming Si', 'Gyorgy Balazs', 'Attila Balazs',
                                                        'Dimitar Grabuloski', 'Sebastien Vidal', 'Julen Uriguen',
                                                        'Martijn Van Haasteren', 'Andreas Vinciguerra', 'Franko Skugor',
                                                        'Ervin Eleskovic', 'Maximo Gonzalez', 'Alexander Sadecky',
                                                        'Andreas Haider Maurer', 'Tim Smyczek', 'Dmitry Tursunov',
                                                        'Kristof Vliegen', 'Peter Polansky', 'Benoit Paire',
                                                        'Adrian Mannarino', 'Adrian Ungur', 'Victor Crivoi',
                                                        'Treat Conrad Huey', 'Suk Young Jeong', 'Jerzy Janowicz',
                                                        'Milos Raonic', 'Michael Venus', 'Uladzimir Ignatik',
                                                        'Simone Vagnozzi', 'Yuki Bhambri', 'Ruben Bemelmans', 'Yan Bai',
                                                        'Michael Ryderstedt', 'Matthias Bachinger',
                                                        'Konstantin Kravchuk',
                                                        'Evgeny Donskoy', 'Robert Kendrick', 'David Goffin',
                                                        'Yuichi Sugita', 'Alexander Kudryavtsev', 'Jan Hernych',
                                                        'Alex Bogomolov Jr', 'Jesse Huta Galung', 'Denis Gremelmayr',
                                                        'Fritz Wolmarans', 'Caio Zampieri', 'Juan Pablo Brzezicki',
                                                        'Lukas Rosol', 'Santiago Gonzalez', 'Joachim Johansson',
                                                        'Soong Jae Cho', 'Shahin Khaledan', 'Anoosha Shahgholi',
                                                        'Jonathan Chu', 'Amer Delic', 'Duilio Beretta',
                                                        'Danai Udomchoke',
                                                        'Alex Llompart', 'Olivier Sajous', 'Marc Abdulnour',
                                                        'Artem Sitak',
                                                        'Amir Weintraub', 'Marcin Gawron', 'Dimitar Kutrovsky',
                                                        'Alexander Bury', 'Jean Rene Lisnard', 'Victor Estrella',
                                                        'Luis Delgado', 'Aqeel Khan', 'Marton Fucsovics',
                                                        'Konstantinos Economidis', 'Deniss Pavlovs', 'Andis Juska',
                                                        'Malek Jaziri', 'Jaak Poldma', 'Mao Xin Gong', 'Flavio Cipolla',
                                                        'Dusan Lajovic', 'Maxime Teixeira', 'Thomas Schoorel',
                                                        'Javier Marti', 'Michael Yani', 'Jimmy Wang', 'Gonzales Austin',
                                                        'Chris Brandi', 'Gabriel Flores Ruiz', 'West Nott',
                                                        'Yassine Idmbarek', 'Kyu Tae Im', 'Young Jun Kim',
                                                        'Hicham Khaddari', 'Vasek Pospisil', 'Julio Cesar Campozano',
                                                        'Ivan Endara', 'Marcus Daniell', 'Philip Bester',
                                                        'Rogerio Dutra Silva', 'Coenie Van Wyk', 'Bruno Abdel Nour',
                                                        'Nicholas Sayer', 'Theodoros Angelinos', 'Dimitar Kuzmanov',
                                                        'Bruno Soares', 'Cedrik Marcel Stebe', 'Pavol Cervenak',
                                                        'Federico Delbonis', 'Jonathan Dasnieres De Veigy',
                                                        'Diego Junqueira', 'Guillermo Olaso', 'Bastian Knittel',
                                                        'Gianluca Naso', 'Daniel Kosakowski', 'Chris Guccione',
                                                        'Pierre Ludovic Duclos', 'Jack Sock', 'Daniele Bracciali',
                                                        'Alexander Peya', 'Nikola Mektic', 'Jeson Patrombon', 'Ti Chen',
                                                        'Grzegorz Panfil', 'Miguel Gallardo Valles', 'Colin Fleming',
                                                        'Nicolas Renavand', 'Mathieu Rodrigues', 'Marius Copil',
                                                        'Alessandro Giannessi', 'Sebastian Rieschick', 'Dominic Thiem',
                                                        'Robert Farah', 'James Duckworth', 'Bobby Reynolds',
                                                        'Luis David Martinez', 'Ricardo Rodriguez', 'Vimuktha De Alwis',
                                                        'Enrique Olivares', 'Denys Molchanov', 'Johnny Arcilla',
                                                        'Manuel Sanchez', 'Sam Barry', 'Janez Semrajc',
                                                        'Liang Chi Huang',
                                                        'Min Hyoek Cho', 'Daniel Evans', 'Martin Cuevas', 'Darian King',
                                                        'Karim Mohamed Maamoun', 'Roberto Cid', 'Federico Zeballos',
                                                        'Haydn Lewis', 'Jose Benitez', 'Radu Albot', 'Dzmitry Zhyrmont',
                                                        'Younes Rachidi', 'Bassam Beidas', 'Albano Olivetti',
                                                        'Facundo Bagnis', 'Roberto Bautista Agut', 'Wisnu Adi Nugroho',
                                                        'Maxim Dubarenco', 'Francis Casey Alcantara',
                                                        'Vladyslav Manafov',
                                                        'Laurent Bram', 'Antso Rakotondramanga', 'Ruan Roelofse',
                                                        'Daniel Llarenas', 'Patrick Chucri', 'Karim Alayli',
                                                        'Kevin Kung',
                                                        'Juan Carlos Ramirez', 'Sergio Gutierrez Ferrol',
                                                        'Lamine Ouahab',
                                                        'Inigo Cervantes Huegun', 'Brian Baker', 'Nicolas Devilder',
                                                        'Mate Pavic', 'Kenny De Schepper', 'Marco Trungelliti',
                                                        'Steve Johnson', 'Philipp Oswald', 'Michael Mcclune',
                                                        'Dennis Novikov', 'Bradley Klahn', 'Emilio Gomez',
                                                        'Vishnu Vardhan', 'Roberto Quiroz', 'Jose Hernandez',
                                                        'Sanam Singh', 'Clement Reix', 'Vincent Millot',
                                                        'Hiroki Moriya',
                                                        'Patrik Rosenholm', 'John Millman', 'Mohamed Safwat',
                                                        'Prakash Amritraj', 'Greg Jones', 'Andre Gaspar Murta',
                                                        'Christopher Diaz Figueroa', 'Jorge Brian Panta Herreros',
                                                        'Issam Al Tawil', 'Ruben Gonzales', 'Henri Laaksonen',
                                                        'Christian Garay', 'Tomislav Ternar', 'Yasutaka Uchiyama',
                                                        'Ji Sung Nam', 'Sarvar Ikramov', 'Miguel Angel Reyes Varela',
                                                        'Dovydas Sakinis', 'Pruchya Isarow', 'Abdullah Maqdas',
                                                        'Lukas Mugevicius', 'Ugo Nastasi', 'Micke Kontinen',
                                                        'Harri Heliovaara', 'Arnau Brugues Davi', 'Cristian Garin',
                                                        'Martin Alund', 'Guido Pella', 'Matteo Viola', 'Rhyne Williams',
                                                        'Diego Schwartzman', 'Rogelio Siller', 'Daniel Glancy',
                                                        'Colin Obrien', 'Egor Gerasimov', 'Gastao Elias',
                                                        'Mohammad Ghareeb', 'Gilles Kremer', 'Luciano Ramazzini',
                                                        'Petros Chrysochos', 'Alexis Klegou', 'Tihomir Grozdanov',
                                                        'Markus Eriksson', 'Pablo Carreno Busta', 'Andre Ghem',
                                                        'Lucas Pouille', 'Nick Kyrgios', 'Mirza Basic', 'Kyle Edmund',
                                                        'Jan Lennard Struff', 'Nils Langer', 'Alex Kuznetsov',
                                                        'Christian Harrison', 'Sam Groth', 'Filip Peliwo',
                                                        'Peter Gojowczyk', 'Marc Lopez', 'Gonzalo Escobar',
                                                        'Nicolaas Scholtz', 'Andrej Martin', 'Herkko Pollanen',
                                                        'Karen Khachanov', 'Jaroslav Pospisil', 'Miloslav Mecir Jr',
                                                        'Pierre Hugues Herbert', 'Ramkumar Ramanathan', 'Jiri Vesely',
                                                        'Thanasi Kokkinakis', 'Romain Arneodo', 'Juan Borba',
                                                        'Mantas Bugailiskis', 'Aditya Hari Sasongko',
                                                        'Frederico Ferreira Silva', 'Santiago Maresca', 'Jose Olivares',
                                                        'Saketh Myneni', 'Mikael Torpegaard', 'Gonzalo Lama',
                                                        'John Morrissey', 'Markos Kalovelonis', 'Taro Daniel',
                                                        'Thien Nguyen Hoang', 'Linh Giang Trinh',
                                                        'Nutthanon Kadchapanan',
                                                        'Wishaya Trongcharoenchaikul', 'Phillip King',
                                                        'Alejandro Gonzalez', 'Patrick Tierro', 'Seanon Williams',
                                                        'Warit Sornbutnark', 'Minh Quan Do', 'Norbert Gombos',
                                                        'Borna Coric', 'Peter Bertran', 'Ayoub Chakrouni',
                                                        'Sergis Kyratzis', 'Mazen Osama', 'Alexandros Jakupovic',
                                                        'Roberto Carballes Baena', 'Aleksandr Nedovyesov',
                                                        'Ognian Kolev',
                                                        'Mate Delic', 'Jason Kubler', 'Nikola Milojevic', 'Axel Michon',
                                                        'Luke Saville', 'Tim Puetz', 'Ante Pavic', 'Philip Davydenko',
                                                        'Yann Marti', 'Renzo Olivo', 'Christian Lindell', 'Elias Ymer',
                                                        'Austin Krajicek', 'Alexander Zverev', 'Rodrigo Senattore',
                                                        'Hyeon Chung', 'Andrey Rublev', 'Tigre Hank', 'Samir Iftikhar',
                                                        'Nerman Fatic', 'Chuhan Wang', 'Nikoloz Basilashvili',
                                                        'Gerald Melzer', 'Nicolas Jarry', 'Luca Vanni',
                                                        'Jared Donaldson',
                                                        'Yoshihito Nishioka', 'Guido Andreozzi', 'Facundo Arguello',
                                                        'Chieh Fu Wang', 'Jui Chen Hung', 'Cem Ilkel', 'Joao Domingues',
                                                        'Tomislav Brkic', 'Benjamin Lock', 'Jan Mertl',
                                                        'Lofo Ramiaramanana', 'Alexandar Lazov', 'Martins Podzus',
                                                        'Hans Podlipnik Castillo', 'Gabor Borsos', 'Arthur De Greef',
                                                        'Matteo Donati', 'Gianni Mina', 'Andrea Arnaboldi',
                                                        'Taylor Fritz',
                                                        'Liam Broady', 'John Patrick Smith', 'M Abid Ali Khan Akbar',
                                                        'Takanyi Garanganga', 'Kimmer Coppejans',
                                                        'Jean Jacques Rakotohasy', 'Alex Diaz', 'Tucker Vorster',
                                                        'Juan Carlos Saez', 'Peter Nagy', 'Hady Habib',
                                                        'Sharmal Dissanayake', 'Seong Chan Hong', 'Aljaz Radinski',
                                                        'Nik Razborsek', 'Oliver Marach', 'Bastian Trinker',
                                                        'Daniel Elahi Galan', 'Adrian Menendez Maceiras',
                                                        'Marcelo Demoliner', 'Alejandro Gomez Gb42',
                                                        'Alexander Sarkissian', 'Jaume Munar', 'Dennis Novak',
                                                        'Frances Tiafoe', 'Zhe Li', 'Marat Deviatiarov',
                                                        'Zhizhen Zhang',
                                                        'Aslan Karatsev', 'Nicolas Xiviller', 'Thomas Fabbiano',
                                                        'Jordan Thompson', 'Matthew Barton', 'Quentin Halys',
                                                        'Omar Jasika', 'Noah Rubin', 'Thiago Monteiro',
                                                        'Alexandar Lazarov', 'Ilya Ivashka', 'Christian Sigsgaard',
                                                        'Benjamin Hannestad', 'Viktor Durasovic', 'Casper Ruud',
                                                        'Lucas Gomez', 'Hans Hach Verdugo', 'Wilfredo Gonzalez',
                                                        'Mikelis Libietis', 'Marco Cecchinato', 'Edan Leshem',
                                                        'Lucas Catarina', 'Hubert Hurkacz', 'Nam Hoang Ly',
                                                        'Miguel Angel Este', 'Sebastian Arcila', 'Ignacio Garcia',
                                                        'Lloyd Harris', 'Juan Pablo Varillas', 'Mohd Assri Merzuki',
                                                        'Bjorn Fratangelo', 'Jozef Kovalik', 'Tommy Paul',
                                                        'Mathias Bourgue', 'Adam Pavlasek', 'Stefan Kozlov',
                                                        'Daniil Medvedev', 'Ernesto Escobedo', 'Marcus Willis',
                                                        'Nicolas Kicker', 'Carl Soderlund', 'Louis Wessels',
                                                        'Calvin Hemery', 'Matwe Middelkoop', 'Yaraslav Shyla',
                                                        'Nicolas Alvarez', 'Nikola Cacic', 'Tristan Lamasine',
                                                        'Steven Diez', 'Denis Shapovalov', 'Reilly Opelka',
                                                        'Jan Satral',
                                                        'Kamil Majchrzak', 'Antoine Bellier', 'Kuan Yi Lee',
                                                        'Joris De Loore', 'Andrew Whittington', 'Mikael Ymer',
                                                        'Alexander Bublik', 'Alex De Minaur', 'Brydan Klein',
                                                        'Isak Arvidsson', 'Karan Rastogi', 'Altug Celikbilek',
                                                        'Hong Kit Jack Wong', 'Simen Sunde Bratholm',
                                                        'Hamid Reza Nadaf',
                                                        'Soren Hess Olesen', 'Tomas Barrios Vera',
                                                        'Jirat Navasirisomboon',
                                                        'Alberto Lim', 'George Tsivadze', 'Jordi Munoz Abreu',
                                                        'Ayed Zatar', 'Bruno Britez', 'Rodrigo Banzer', 'Federico Gaio',
                                                        'Giovanni Lapentti', 'Yibing Wu', 'August Holmgren',
                                                        'Temur Ismailov', 'Dmitry Popko', 'Prajnesh Gunneswaran',
                                                        'Amine Ahouda', 'Gianluigi Quinzi', 'Laslo Djere',
                                                        'Yannick Hanfmann', 'Stefano Napolitano', 'Benjamin Bonzi',
                                                        'Daniel Altmaier', 'Cameron Norrie', 'Sebastian Ofner',
                                                        'Akira Santillan', 'Christopher Eubanks', 'Gleb Sakharov',
                                                        'Tennys Sandgren', 'Miljan Zekic', 'Evan King',
                                                        'Mitchell Krueger',
                                                        'Stefano Travaglia', 'Viktor Galovic', 'Yannick Maden',
                                                        'Stefanos Tsitsipas', 'Ricardo Ojeda Lara', 'Michael Mmoh',
                                                        'Matteo Berrettini', 'Maximilian Marterer',
                                                        'Mackenzie Mcdonald',
                                                        'Lorenzo Sonego', 'Zsombor Piros', 'Marc Andrea Huesler',
                                                        'Pedja Krstin', 'Cristian Rodriguez', 'Joao Pedro Sorgi',
                                                        'Bogdan Borza', 'John Bryan Decasa Otico', 'Luis Patino',
                                                        'Emil Ruusuvuori', 'Sarp Agabigun',
                                                        'Luis Diego Chavez Villalpando', 'Youssef Hossam',
                                                        'Rodrigo Arus',
                                                        'Chun Hsin Tseng', 'Benjamin Hassan', 'Peter Bothwell',
                                                        'Skyler Butts', 'Anthony Jackie Tang', 'Corentin Moutet',
                                                        'Carlos Taberner', 'Tallon Griekspoor', 'Guilherme Clezar',
                                                        'Felix Auger Aliassime', 'Nicola Kuhn', 'Khumoun Sultanov',
                                                        'Yshai Oliel', 'Dragos Dima', 'Edris Fetisleam',
                                                        'Palaphoom Kovapitukted', 'Francisco Llanes',
                                                        'Daniel Michalski',
                                                        'Holger Rune', 'Gerardo Lopez Villasenor', 'Alexey Vatutin',
                                                        'Filip Horansky', 'Bernabe Zapata Miralles', 'Federico Coria',
                                                        'Rudolf Molleker', 'Alex Bolt', 'Jay Clarke', 'Jason Jung',
                                                        'Daniel Masur', 'Oriol Roca Batalla', 'Marcos Giron',
                                                        'Dominik Koepfer', 'Ugo Humbert', 'Yosuke Watanuki',
                                                        'Jonathan Mridha', 'Jurabek Karimov', 'Constant Lestienne',
                                                        'Oscar Otte', 'Salvatore Caruso', 'Alexei Popyrin',
                                                        'Miomir Kecmanovic', 'Antoine Hoang', 'Juan Ignacio Londero',
                                                        'Pedro Cachin', 'Brayden Schnur', 'Gregoire Barrere',
                                                        'Thiago Seyboth Wild', 'Filip Cristian Jianu', 'Jannik Sinner',
                                                        'Alejandro Davidovich Fokina', 'Elliot Benchetrit',
                                                        'Kevin Krawietz', 'Nino Serdarusic', 'Soon Woo Kwon',
                                                        'Gian Marco Moroni', 'Kevin King', 'Marc Polmans',
                                                        'Duck Hee Lee',
                                                        'Jenson Brooksby', 'Sanjar Fayziev', 'Sandro Ehrat',
                                                        'Philip Henning', 'Aleksandre Metreveli', 'Cayetano March',
                                                        'Jonas Forejtek', 'Ajeet Rai', 'Rhett Purcell', 'Ari Fahresi',
                                                        'Tung Lin Wu', 'Gianluca Mager', 'Alen Avidzba', 'Kacper Zuk',
                                                        'Pedro Martinez', 'Alejandro Tabilo', 'Roberto Marcora',
                                                        'Brandon Nakashima', 'Carlos Alcaraz', 'Blaise Bicknell',
                                                        'Alexander Donski', 'Finn Tearney', 'Daniel Cukierman',
                                                        'Kristjan Tamm', 'Daniil Glinka', 'Hazem Naw',
                                                        'Maks Kasnikowski',
                                                        'Petros Tsitsipas', 'Adolfo Daniel Vallejo',
                                                        'Martin Antonio Vergara Del Puerto', 'Aissa Benchakroun',
                                                        'Robert Strombachs', 'Gunawan Trismuwantara', 'Adam Moundir',
                                                        'Lukas Hellum Lilleengen', 'Borna Gojo', 'Otto Virtanen',
                                                        'Patrik Niklas Salminen', 'J J Wolf', 'Maxime Cressy',
                                                        'Sumit Nagal', 'Christopher Oconnell', 'Lorenzo Musetti',
                                                        'Hugo Gaston', 'Sebastian Korda', 'Jurij Rodionov',
                                                        'Lorenzo Giustino', 'Andrea Pellegrino', 'Roman Safiullin',
                                                        'Danilo Petrovic', 'Zizou Bergs', 'Adrian Andreev',
                                                        'Hugo Grenier',
                                                        'Mario Vilella Martinez', 'Botic Van De Zandschulp',
                                                        'Aleksandar Vukic', 'Dane Sweeny', 'Andrew Harris',
                                                        'Harry Bourchier', 'Max Purcell', 'Tomas Machac',
                                                        'Alexandre Muller', 'Juan Manuel Cerundolo',
                                                        'Francisco Cerundolo',
                                                        'Tomas Martin Etcheverry', 'Lukas Klein', 'Kaichi Uchida',
                                                        'Yuta Shimizu', 'Arthur Rinderknech', 'Nuno Borges',
                                                        'Dominic Stricker', 'Arthur Cazaux', 'Flavio Cobolli',
                                                        'Mats Moraing', 'Alex Molcan', 'Enzo Couacaud', 'Jack Draper',
                                                        'Sebastian Baez', 'Vit Kopriva', 'Duje Ajdukovic',
                                                        'Alexander Erler', 'Zachary Svajda', 'Jerome Kym',
                                                        'Hernando Jose Escurra Isnardi', 'Tom Kocevar Desman',
                                                        'Aziz Dougaz', 'Nick Hardt', 'Justin Barki', 'Bor Artnak ',
                                                        'Kasidit Samrej', 'Jisung Nam', 'Michael Geerts',
                                                        'Murkel Alejandro Dellien Velasco', 'Ergi Kirkin',
                                                        'Daniil Ostapenkov', 'Felipe Meligeni Alves',
                                                        'Matheus Pucinelli De Almeida', 'Orlando Luz',
                                                        'Alexandros Skorilas', 'Timofey Skatov', 'Andrea Vavassori',
                                                        'Aziz Ouakaa', 'Michail Pervolarakis', 'Juan Pablo Ficovich',
                                                        'Jiri Lehecka', 'Sylvestre Monnou', 'Coleman Wong',
                                                        'Aristotelis Thanos', 'Amr Elsayed Abdou Ahmed Mohamed',
                                                        'Rowland Phillips', 'Pavel Kotov', 'Gijs Brouwer',
                                                        'Manuel Guinard', 'Johan Nikles', 'Camilo Ugo Carabelli',
                                                        'Zdenek Kolar', 'Tim Van Rijthoven', 'Ryan Peniston']))

with col2:
    second_player = st.selectbox('Second player', sorted(['Radek Stepanek',
                                                          'Andy Roddick', 'Gael Monfils', 'Tomas Berdych',
                                                          'Wayne Odesnik', 'Thomaz Bellucci', 'Richard Gasquet',
                                                          'Alexandr Dolgopolov', 'James Blake', 'Alejandro Falla',
                                                          'Carsten Ball', 'Matthew Ebden', 'Marcos Baghdatis',
                                                          'Marc Gicquel', 'Florent Serra', 'Harel Levy', 'Lukasz Kubot',
                                                          'Potito Starace', 'Younes El Aynaoui', 'Steve Darcis',
                                                          'Sergiy Stakhovsky', 'Olivier Rochus', 'Ernests Gulbis',
                                                          'Ivo Karlovic', 'Benjamin Becker', 'Marco Chiudinelli',
                                                          'Nikolay Davydenko', 'Andreas Seppi', 'Rafael Nadal',
                                                          'Viktor Troicki', 'Roger Federer', 'Marin Cilic',
                                                          'Evgeny Korolev',
                                                          'Michael Berrer', 'Robby Ginepri', 'Lukas Lacko', 'Kevin Kim',
                                                          'Dudi Sela', 'Stan Wawrinka', 'Michael Russell',
                                                          'Stephane Robert',
                                                          'Thiemo De Bakker', 'Somdev Devvarman', 'Janko Tipsarevic',
                                                          'Jan Hajek', 'Santiago Giraldo', 'Robin Haase',
                                                          'Marcel Granollers', 'Peter Luczak', 'Mardy Fish',
                                                          'Leonardo Mayer', 'Pablo Cuevas', 'Julien Benneteau',
                                                          'Lleyton Hewitt', 'John Isner', 'Sebastien Grosjean',
                                                          'Arnaud Clement', 'Simon Greul', 'Juan Monaco',
                                                          'Michael Lammer',
                                                          'Jose Rubin Statham', 'Philipp Kohlschreiber',
                                                          'Jurgen Melzer',
                                                          'Albert Montanes', 'Tommy Robredo', 'Fernando Gonzalez',
                                                          'Florian Mayer', 'Andy Murray', 'Feliciano Lopez',
                                                          'Ivan Ljubicic',
                                                          'Juan Martin del Potro', 'Fernando Verdasco',
                                                          'Nicolas Almagro',
                                                          'Tommy Haas', 'Jo-Wilfried Tsonga', 'Mikhail Youzhny',
                                                          'Denis Istomin', 'Novak Djokovic', 'Stefan Koubek',
                                                          'Ivan Dodig',
                                                          'Taylor Dent', 'Michael Llodra', 'Ivan Sergeyev',
                                                          'David Ferrer',
                                                          'Donald Young', 'Victor Hanescu', 'Illya Marchenko',
                                                          'Andrey Golubev', 'Antonio Veic', 'Louk Sorensen',
                                                          'Jarkko Nieminen', 'Marsel Ilhan', 'Rainer Schuettler',
                                                          'Bernard Tomic', 'Igor Kunitsyn', 'Alexandre Sidorenko',
                                                          'Daniel Koellerer', 'Joao Souza', 'Eduardo Schwank',
                                                          'Alberto Martin', 'Philipp Petzschner', 'Mikhail Kukushkin',
                                                          'Petar Jelenic', 'Juan Ignacio Chela', 'Yen Hsun Lu',
                                                          'Filip Prpic', 'Thiago Alves', 'David Marrero',
                                                          'Laurent Recouderc', 'Izak Van Der Merwe', 'Rajeev Ram',
                                                          'Bjorn Phau', 'Blaz Kavcic', 'Raven Klaasen',
                                                          'Josselin Ouanna',
                                                          'Dustin Brown', 'Pere Riba', 'Jose Acasuso',
                                                          'Paul Capdeville',
                                                          'Ricardo Mello', 'Ruben Ramirez Hidalgo', 'Robin Soderling',
                                                          'Xavier Malisse', 'Sam Querrey', 'Ricardas Berankis',
                                                          'Juan Carlos Ferrero', 'Carlos Berlocq', 'Fabio Fognini',
                                                          'Igor Andreev', 'Rui Machado', 'Frederico Gil',
                                                          'Daniel Gimeno Traver', 'Nicolas Massu', 'Igor Sijsling',
                                                          'Mischa Zverev', 'Guillaume Rufin', 'Jeremy Chardy',
                                                          'David Nalbandian', 'Marcos Daniel', 'Santiago Ventura',
                                                          'Carlos Moya', 'Horacio Zeballos', 'Pablo Andujar',
                                                          'Yannick Mertens', 'Daniel Brands', 'Teymuraz Gabashvili',
                                                          'Ramon Delgado', 'Alexander Blom', 'Nicolas Salama',
                                                          'Ivan Miranda', 'Mauricio Echazu',
                                                          'Alvaro Raposo De Oliveira',
                                                          'Pedro Sousa', 'Martin Pedersen', 'Diego Galeano',
                                                          'Daniel King Turner', 'Sergio Galdos', 'Siu Fai Kelvin Lam',
                                                          'Aldin Setkic', 'Aisam Ul Haq Qureshi', 'Hiu Tung Yu',
                                                          'Aljaz Bedene', 'Luka Gregorc', 'Grega Zemlja',
                                                          'Ismar Gorcic',
                                                          'Predrag Rusevski', 'Cesar Ramirez', 'Bruno Rodriguez',
                                                          'Harshana Godamanna', 'Kittipong Wachiramanowong',
                                                          'Sunu Wahyu Trijati', 'Rohan Bopanna',
                                                          'Peerakiat Siriluethaiwattana', 'Lukas Dlouhy',
                                                          'David Agung Susanto', 'Conor Niland', 'Christopher Rungkat',
                                                          'Henri Kontinen', 'Go Soeda', 'Tatsuma Ito',
                                                          'Filippo Volandri',
                                                          'Simone Bolelli', 'Ariel Behar', 'Jhonson Garcia',
                                                          'Marcel Felder',
                                                          'Di Wu', 'Ze Zhang', 'Laurynas Grigelis', 'James Ward',
                                                          'Barry King', 'James Mcgee', 'Vladimir Ivanov', 'Jurgen Zopp',
                                                          'Adam Kellner', 'Sherif Sabry', 'Thomas Oger',
                                                          'Karim Maamoun',
                                                          'Carlos Salamanca', 'Juan Sebastian Cabal', 'Martin Klizan',
                                                          'Roman Recarte', 'Mauricio Doria Medina', 'Piero Luisi',
                                                          'Benjamin Balleret', 'Grigor Dimitrov', 'Yohny Romero',
                                                          'Jorge Aguilar', 'Brian Dabul', 'Guillermo Garcia Lopez',
                                                          'Mario Ancic', 'Paul Henri Mathieu', 'Marinko Matosevic',
                                                          'Kevin Anderson', 'Ryan Harrison', 'Nicolas Lapentti',
                                                          'Ryan Sweeting', 'Reda El Amrani', 'Oscar Hernandez',
                                                          'Ivan Navarro', 'Albert Ramos', 'Paolo Lorenzi',
                                                          'Andreas Beck',
                                                          'Leonardo Tavares', 'Filip Krajinovic', 'Alessio Di Mauro',
                                                          'Rik De Voest', 'Marcelo Melo', 'Daniel Munoz de la Nava',
                                                          'Julian Reister', 'Edouard Roger Vasselin', 'Tobias Kamke',
                                                          'Kei Nishikori', 'Yuri Schukin', 'Nicolas Mahut',
                                                          'Gilles Muller',
                                                          'Jesse Levine', 'Nicolas Kiefer', 'Dominik Meffert',
                                                          'Gilles Simon', 'Andrey Kuznetsov', 'Michal Przysiezny',
                                                          'Karol Beck', 'Brendan Evans', 'Ilija Bozoljac',
                                                          'Martin Fischer',
                                                          'Frank Dancevic', 'Richard Bloomfield', 'Sergei Bubka',
                                                          'Denis Kudla', 'Austen Childs', 'Joao Sousa', 'Daniel Garza',
                                                          'Daniel Alejandro Lopez Cassaccia', 'Weerapat Doakmaiklee',
                                                          'Blaz Rola', 'Damir Dzumhur', 'Ivo Minar', 'David Souto',
                                                          'Jamie Baker', 'Soren Wedege', 'Thomas Kromann',
                                                          'Frederik Nielsen', 'Hugo Dellien', 'Rodrigo Rappaccioli',
                                                          'Marcelo Arevalo', 'Rafael Arevalo', 'Hsin Han Lee',
                                                          'Tsung Hua Yang', 'Yong Kyu Lim', 'Hyun Joon Kim',
                                                          'Farrukh Dustov', 'Cecil Mamiit', 'Dineshkanthan Thangarajah',
                                                          'Martin Sayer', 'Abd Hazli Bin Zainuddin', 'Michael Leong',
                                                          'Yew Ming Si', 'Gyorgy Balazs', 'Attila Balazs',
                                                          'Dimitar Grabuloski', 'Sebastien Vidal', 'Julen Uriguen',
                                                          'Martijn Van Haasteren', 'Andreas Vinciguerra',
                                                          'Franko Skugor',
                                                          'Ervin Eleskovic', 'Maximo Gonzalez', 'Alexander Sadecky',
                                                          'Andreas Haider Maurer', 'Tim Smyczek', 'Dmitry Tursunov',
                                                          'Kristof Vliegen', 'Peter Polansky', 'Benoit Paire',
                                                          'Adrian Mannarino', 'Adrian Ungur', 'Victor Crivoi',
                                                          'Treat Conrad Huey', 'Suk Young Jeong', 'Jerzy Janowicz',
                                                          'Milos Raonic', 'Michael Venus', 'Uladzimir Ignatik',
                                                          'Simone Vagnozzi', 'Yuki Bhambri', 'Ruben Bemelmans',
                                                          'Yan Bai',
                                                          'Michael Ryderstedt', 'Matthias Bachinger',
                                                          'Konstantin Kravchuk',
                                                          'Evgeny Donskoy', 'Robert Kendrick', 'David Goffin',
                                                          'Yuichi Sugita', 'Alexander Kudryavtsev', 'Jan Hernych',
                                                          'Alex Bogomolov Jr', 'Jesse Huta Galung', 'Denis Gremelmayr',
                                                          'Fritz Wolmarans', 'Caio Zampieri', 'Juan Pablo Brzezicki',
                                                          'Lukas Rosol', 'Santiago Gonzalez', 'Joachim Johansson',
                                                          'Soong Jae Cho', 'Shahin Khaledan', 'Anoosha Shahgholi',
                                                          'Jonathan Chu', 'Amer Delic', 'Duilio Beretta',
                                                          'Danai Udomchoke',
                                                          'Alex Llompart', 'Olivier Sajous', 'Marc Abdulnour',
                                                          'Artem Sitak',
                                                          'Amir Weintraub', 'Marcin Gawron', 'Dimitar Kutrovsky',
                                                          'Alexander Bury', 'Jean Rene Lisnard', 'Victor Estrella',
                                                          'Luis Delgado', 'Aqeel Khan', 'Marton Fucsovics',
                                                          'Konstantinos Economidis', 'Deniss Pavlovs', 'Andis Juska',
                                                          'Malek Jaziri', 'Jaak Poldma', 'Mao Xin Gong',
                                                          'Flavio Cipolla',
                                                          'Dusan Lajovic', 'Maxime Teixeira', 'Thomas Schoorel',
                                                          'Javier Marti', 'Michael Yani', 'Jimmy Wang',
                                                          'Gonzales Austin',
                                                          'Chris Brandi', 'Gabriel Flores Ruiz', 'West Nott',
                                                          'Yassine Idmbarek', 'Kyu Tae Im', 'Young Jun Kim',
                                                          'Hicham Khaddari', 'Vasek Pospisil', 'Julio Cesar Campozano',
                                                          'Ivan Endara', 'Marcus Daniell', 'Philip Bester',
                                                          'Rogerio Dutra Silva', 'Coenie Van Wyk', 'Bruno Abdel Nour',
                                                          'Nicholas Sayer', 'Theodoros Angelinos', 'Dimitar Kuzmanov',
                                                          'Bruno Soares', 'Cedrik Marcel Stebe', 'Pavol Cervenak',
                                                          'Federico Delbonis', 'Jonathan Dasnieres De Veigy',
                                                          'Diego Junqueira', 'Guillermo Olaso', 'Bastian Knittel',
                                                          'Gianluca Naso', 'Daniel Kosakowski', 'Chris Guccione',
                                                          'Pierre Ludovic Duclos', 'Jack Sock', 'Daniele Bracciali',
                                                          'Alexander Peya', 'Nikola Mektic', 'Jeson Patrombon',
                                                          'Ti Chen',
                                                          'Grzegorz Panfil', 'Miguel Gallardo Valles', 'Colin Fleming',
                                                          'Nicolas Renavand', 'Mathieu Rodrigues', 'Marius Copil',
                                                          'Alessandro Giannessi', 'Sebastian Rieschick',
                                                          'Dominic Thiem',
                                                          'Robert Farah', 'James Duckworth', 'Bobby Reynolds',
                                                          'Luis David Martinez', 'Ricardo Rodriguez',
                                                          'Vimuktha De Alwis',
                                                          'Enrique Olivares', 'Denys Molchanov', 'Johnny Arcilla',
                                                          'Manuel Sanchez', 'Sam Barry', 'Janez Semrajc',
                                                          'Liang Chi Huang',
                                                          'Min Hyoek Cho', 'Daniel Evans', 'Martin Cuevas',
                                                          'Darian King',
                                                          'Karim Mohamed Maamoun', 'Roberto Cid', 'Federico Zeballos',
                                                          'Haydn Lewis', 'Jose Benitez', 'Radu Albot',
                                                          'Dzmitry Zhyrmont',
                                                          'Younes Rachidi', 'Bassam Beidas', 'Albano Olivetti',
                                                          'Facundo Bagnis', 'Roberto Bautista Agut',
                                                          'Wisnu Adi Nugroho',
                                                          'Maxim Dubarenco', 'Francis Casey Alcantara',
                                                          'Vladyslav Manafov',
                                                          'Laurent Bram', 'Antso Rakotondramanga', 'Ruan Roelofse',
                                                          'Daniel Llarenas', 'Patrick Chucri', 'Karim Alayli',
                                                          'Kevin Kung',
                                                          'Juan Carlos Ramirez', 'Sergio Gutierrez Ferrol',
                                                          'Lamine Ouahab',
                                                          'Inigo Cervantes Huegun', 'Brian Baker', 'Nicolas Devilder',
                                                          'Mate Pavic', 'Kenny De Schepper', 'Marco Trungelliti',
                                                          'Steve Johnson', 'Philipp Oswald', 'Michael Mcclune',
                                                          'Dennis Novikov', 'Bradley Klahn', 'Emilio Gomez',
                                                          'Vishnu Vardhan', 'Roberto Quiroz', 'Jose Hernandez',
                                                          'Sanam Singh', 'Clement Reix', 'Vincent Millot',
                                                          'Hiroki Moriya',
                                                          'Patrik Rosenholm', 'John Millman', 'Mohamed Safwat',
                                                          'Prakash Amritraj', 'Greg Jones', 'Andre Gaspar Murta',
                                                          'Christopher Diaz Figueroa', 'Jorge Brian Panta Herreros',
                                                          'Issam Al Tawil', 'Ruben Gonzales', 'Henri Laaksonen',
                                                          'Christian Garay', 'Tomislav Ternar', 'Yasutaka Uchiyama',
                                                          'Ji Sung Nam', 'Sarvar Ikramov', 'Miguel Angel Reyes Varela',
                                                          'Dovydas Sakinis', 'Pruchya Isarow', 'Abdullah Maqdas',
                                                          'Lukas Mugevicius', 'Ugo Nastasi', 'Micke Kontinen',
                                                          'Harri Heliovaara', 'Arnau Brugues Davi', 'Cristian Garin',
                                                          'Martin Alund', 'Guido Pella', 'Matteo Viola',
                                                          'Rhyne Williams',
                                                          'Diego Schwartzman', 'Rogelio Siller', 'Daniel Glancy',
                                                          'Colin Obrien', 'Egor Gerasimov', 'Gastao Elias',
                                                          'Mohammad Ghareeb', 'Gilles Kremer', 'Luciano Ramazzini',
                                                          'Petros Chrysochos', 'Alexis Klegou', 'Tihomir Grozdanov',
                                                          'Markus Eriksson', 'Pablo Carreno Busta', 'Andre Ghem',
                                                          'Lucas Pouille', 'Nick Kyrgios', 'Mirza Basic', 'Kyle Edmund',
                                                          'Jan Lennard Struff', 'Nils Langer', 'Alex Kuznetsov',
                                                          'Christian Harrison', 'Sam Groth', 'Filip Peliwo',
                                                          'Peter Gojowczyk', 'Marc Lopez', 'Gonzalo Escobar',
                                                          'Nicolaas Scholtz', 'Andrej Martin', 'Herkko Pollanen',
                                                          'Karen Khachanov', 'Jaroslav Pospisil', 'Miloslav Mecir Jr',
                                                          'Pierre Hugues Herbert', 'Ramkumar Ramanathan', 'Jiri Vesely',
                                                          'Thanasi Kokkinakis', 'Romain Arneodo', 'Juan Borba',
                                                          'Mantas Bugailiskis', 'Aditya Hari Sasongko',
                                                          'Frederico Ferreira Silva', 'Santiago Maresca',
                                                          'Jose Olivares',
                                                          'Saketh Myneni', 'Mikael Torpegaard', 'Gonzalo Lama',
                                                          'John Morrissey', 'Markos Kalovelonis', 'Taro Daniel',
                                                          'Thien Nguyen Hoang', 'Linh Giang Trinh',
                                                          'Nutthanon Kadchapanan',
                                                          'Wishaya Trongcharoenchaikul', 'Phillip King',
                                                          'Alejandro Gonzalez', 'Patrick Tierro', 'Seanon Williams',
                                                          'Warit Sornbutnark', 'Minh Quan Do', 'Norbert Gombos',
                                                          'Borna Coric', 'Peter Bertran', 'Ayoub Chakrouni',
                                                          'Sergis Kyratzis', 'Mazen Osama', 'Alexandros Jakupovic',
                                                          'Roberto Carballes Baena', 'Aleksandr Nedovyesov',
                                                          'Ognian Kolev',
                                                          'Mate Delic', 'Jason Kubler', 'Nikola Milojevic',
                                                          'Axel Michon',
                                                          'Luke Saville', 'Tim Puetz', 'Ante Pavic', 'Philip Davydenko',
                                                          'Yann Marti', 'Renzo Olivo', 'Christian Lindell',
                                                          'Elias Ymer',
                                                          'Austin Krajicek', 'Alexander Zverev', 'Rodrigo Senattore',
                                                          'Hyeon Chung', 'Andrey Rublev', 'Tigre Hank',
                                                          'Samir Iftikhar',
                                                          'Nerman Fatic', 'Chuhan Wang', 'Nikoloz Basilashvili',
                                                          'Gerald Melzer', 'Nicolas Jarry', 'Luca Vanni',
                                                          'Jared Donaldson',
                                                          'Yoshihito Nishioka', 'Guido Andreozzi', 'Facundo Arguello',
                                                          'Chieh Fu Wang', 'Jui Chen Hung', 'Cem Ilkel',
                                                          'Joao Domingues',
                                                          'Tomislav Brkic', 'Benjamin Lock', 'Jan Mertl',
                                                          'Lofo Ramiaramanana', 'Alexandar Lazov', 'Martins Podzus',
                                                          'Hans Podlipnik Castillo', 'Gabor Borsos', 'Arthur De Greef',
                                                          'Matteo Donati', 'Gianni Mina', 'Andrea Arnaboldi',
                                                          'Taylor Fritz',
                                                          'Liam Broady', 'John Patrick Smith', 'M Abid Ali Khan Akbar',
                                                          'Takanyi Garanganga', 'Kimmer Coppejans',
                                                          'Jean Jacques Rakotohasy', 'Alex Diaz', 'Tucker Vorster',
                                                          'Juan Carlos Saez', 'Peter Nagy', 'Hady Habib',
                                                          'Sharmal Dissanayake', 'Seong Chan Hong', 'Aljaz Radinski',
                                                          'Nik Razborsek', 'Oliver Marach', 'Bastian Trinker',
                                                          'Daniel Elahi Galan', 'Adrian Menendez Maceiras',
                                                          'Marcelo Demoliner', 'Alejandro Gomez Gb42',
                                                          'Alexander Sarkissian', 'Jaume Munar', 'Dennis Novak',
                                                          'Frances Tiafoe', 'Zhe Li', 'Marat Deviatiarov',
                                                          'Zhizhen Zhang',
                                                          'Aslan Karatsev', 'Nicolas Xiviller', 'Thomas Fabbiano',
                                                          'Jordan Thompson', 'Matthew Barton', 'Quentin Halys',
                                                          'Omar Jasika', 'Noah Rubin', 'Thiago Monteiro',
                                                          'Alexandar Lazarov', 'Ilya Ivashka', 'Christian Sigsgaard',
                                                          'Benjamin Hannestad', 'Viktor Durasovic', 'Casper Ruud',
                                                          'Lucas Gomez', 'Hans Hach Verdugo', 'Wilfredo Gonzalez',
                                                          'Mikelis Libietis', 'Marco Cecchinato', 'Edan Leshem',
                                                          'Lucas Catarina', 'Hubert Hurkacz', 'Nam Hoang Ly',
                                                          'Miguel Angel Este', 'Sebastian Arcila', 'Ignacio Garcia',
                                                          'Lloyd Harris', 'Juan Pablo Varillas', 'Mohd Assri Merzuki',
                                                          'Bjorn Fratangelo', 'Jozef Kovalik', 'Tommy Paul',
                                                          'Mathias Bourgue', 'Adam Pavlasek', 'Stefan Kozlov',
                                                          'Daniil Medvedev', 'Ernesto Escobedo', 'Marcus Willis',
                                                          'Nicolas Kicker', 'Carl Soderlund', 'Louis Wessels',
                                                          'Calvin Hemery', 'Matwe Middelkoop', 'Yaraslav Shyla',
                                                          'Nicolas Alvarez', 'Nikola Cacic', 'Tristan Lamasine',
                                                          'Steven Diez', 'Denis Shapovalov', 'Reilly Opelka',
                                                          'Jan Satral',
                                                          'Kamil Majchrzak', 'Antoine Bellier', 'Kuan Yi Lee',
                                                          'Joris De Loore', 'Andrew Whittington', 'Mikael Ymer',
                                                          'Alexander Bublik', 'Alex De Minaur', 'Brydan Klein',
                                                          'Isak Arvidsson', 'Karan Rastogi', 'Altug Celikbilek',
                                                          'Hong Kit Jack Wong', 'Simen Sunde Bratholm',
                                                          'Hamid Reza Nadaf',
                                                          'Soren Hess Olesen', 'Tomas Barrios Vera',
                                                          'Jirat Navasirisomboon',
                                                          'Alberto Lim', 'George Tsivadze', 'Jordi Munoz Abreu',
                                                          'Ayed Zatar', 'Bruno Britez', 'Rodrigo Banzer',
                                                          'Federico Gaio',
                                                          'Giovanni Lapentti', 'Yibing Wu', 'August Holmgren',
                                                          'Temur Ismailov', 'Dmitry Popko', 'Prajnesh Gunneswaran',
                                                          'Amine Ahouda', 'Gianluigi Quinzi', 'Laslo Djere',
                                                          'Yannick Hanfmann', 'Stefano Napolitano', 'Benjamin Bonzi',
                                                          'Daniel Altmaier', 'Cameron Norrie', 'Sebastian Ofner',
                                                          'Akira Santillan', 'Christopher Eubanks', 'Gleb Sakharov',
                                                          'Tennys Sandgren', 'Miljan Zekic', 'Evan King',
                                                          'Mitchell Krueger',
                                                          'Stefano Travaglia', 'Viktor Galovic', 'Yannick Maden',
                                                          'Stefanos Tsitsipas', 'Ricardo Ojeda Lara', 'Michael Mmoh',
                                                          'Matteo Berrettini', 'Maximilian Marterer',
                                                          'Mackenzie Mcdonald',
                                                          'Lorenzo Sonego', 'Zsombor Piros', 'Marc Andrea Huesler',
                                                          'Pedja Krstin', 'Cristian Rodriguez', 'Joao Pedro Sorgi',
                                                          'Bogdan Borza', 'John Bryan Decasa Otico', 'Luis Patino',
                                                          'Emil Ruusuvuori', 'Sarp Agabigun',
                                                          'Luis Diego Chavez Villalpando', 'Youssef Hossam',
                                                          'Rodrigo Arus',
                                                          'Chun Hsin Tseng', 'Benjamin Hassan', 'Peter Bothwell',
                                                          'Skyler Butts', 'Anthony Jackie Tang', 'Corentin Moutet',
                                                          'Carlos Taberner', 'Tallon Griekspoor', 'Guilherme Clezar',
                                                          'Felix Auger Aliassime', 'Nicola Kuhn', 'Khumoun Sultanov',
                                                          'Yshai Oliel', 'Dragos Dima', 'Edris Fetisleam',
                                                          'Palaphoom Kovapitukted', 'Francisco Llanes',
                                                          'Daniel Michalski',
                                                          'Holger Rune', 'Gerardo Lopez Villasenor', 'Alexey Vatutin',
                                                          'Filip Horansky', 'Bernabe Zapata Miralles', 'Federico Coria',
                                                          'Rudolf Molleker', 'Alex Bolt', 'Jay Clarke', 'Jason Jung',
                                                          'Daniel Masur', 'Oriol Roca Batalla', 'Marcos Giron',
                                                          'Dominik Koepfer', 'Ugo Humbert', 'Yosuke Watanuki',
                                                          'Jonathan Mridha', 'Jurabek Karimov', 'Constant Lestienne',
                                                          'Oscar Otte', 'Salvatore Caruso', 'Alexei Popyrin',
                                                          'Miomir Kecmanovic', 'Antoine Hoang', 'Juan Ignacio Londero',
                                                          'Pedro Cachin', 'Brayden Schnur', 'Gregoire Barrere',
                                                          'Thiago Seyboth Wild', 'Filip Cristian Jianu',
                                                          'Jannik Sinner',
                                                          'Alejandro Davidovich Fokina', 'Elliot Benchetrit',
                                                          'Kevin Krawietz', 'Nino Serdarusic', 'Soon Woo Kwon',
                                                          'Gian Marco Moroni', 'Kevin King', 'Marc Polmans',
                                                          'Duck Hee Lee',
                                                          'Jenson Brooksby', 'Sanjar Fayziev', 'Sandro Ehrat',
                                                          'Philip Henning', 'Aleksandre Metreveli', 'Cayetano March',
                                                          'Jonas Forejtek', 'Ajeet Rai', 'Rhett Purcell', 'Ari Fahresi',
                                                          'Tung Lin Wu', 'Gianluca Mager', 'Alen Avidzba', 'Kacper Zuk',
                                                          'Pedro Martinez', 'Alejandro Tabilo', 'Roberto Marcora',
                                                          'Brandon Nakashima', 'Carlos Alcaraz', 'Blaise Bicknell',
                                                          'Alexander Donski', 'Finn Tearney', 'Daniel Cukierman',
                                                          'Kristjan Tamm', 'Daniil Glinka', 'Hazem Naw',
                                                          'Maks Kasnikowski',
                                                          'Petros Tsitsipas', 'Adolfo Daniel Vallejo',
                                                          'Martin Antonio Vergara Del Puerto', 'Aissa Benchakroun',
                                                          'Robert Strombachs', 'Gunawan Trismuwantara', 'Adam Moundir',
                                                          'Lukas Hellum Lilleengen', 'Borna Gojo', 'Otto Virtanen',
                                                          'Patrik Niklas Salminen', 'J J Wolf', 'Maxime Cressy',
                                                          'Sumit Nagal', 'Christopher Oconnell', 'Lorenzo Musetti',
                                                          'Hugo Gaston', 'Sebastian Korda', 'Jurij Rodionov',
                                                          'Lorenzo Giustino', 'Andrea Pellegrino', 'Roman Safiullin',
                                                          'Danilo Petrovic', 'Zizou Bergs', 'Adrian Andreev',
                                                          'Hugo Grenier',
                                                          'Mario Vilella Martinez', 'Botic Van De Zandschulp',
                                                          'Aleksandar Vukic', 'Dane Sweeny', 'Andrew Harris',
                                                          'Harry Bourchier', 'Max Purcell', 'Tomas Machac',
                                                          'Alexandre Muller', 'Juan Manuel Cerundolo',
                                                          'Francisco Cerundolo',
                                                          'Tomas Martin Etcheverry', 'Lukas Klein', 'Kaichi Uchida',
                                                          'Yuta Shimizu', 'Arthur Rinderknech', 'Nuno Borges',
                                                          'Dominic Stricker', 'Arthur Cazaux', 'Flavio Cobolli',
                                                          'Mats Moraing', 'Alex Molcan', 'Enzo Couacaud', 'Jack Draper',
                                                          'Sebastian Baez', 'Vit Kopriva', 'Duje Ajdukovic',
                                                          'Alexander Erler', 'Zachary Svajda', 'Jerome Kym',
                                                          'Hernando Jose Escurra Isnardi', 'Tom Kocevar Desman',
                                                          'Aziz Dougaz', 'Nick Hardt', 'Justin Barki', 'Bor Artnak ',
                                                          'Kasidit Samrej', 'Jisung Nam', 'Michael Geerts',
                                                          'Murkel Alejandro Dellien Velasco', 'Ergi Kirkin',
                                                          'Daniil Ostapenkov', 'Felipe Meligeni Alves',
                                                          'Matheus Pucinelli De Almeida', 'Orlando Luz',
                                                          'Alexandros Skorilas', 'Timofey Skatov', 'Andrea Vavassori',
                                                          'Aziz Ouakaa', 'Michail Pervolarakis', 'Juan Pablo Ficovich',
                                                          'Jiri Lehecka', 'Sylvestre Monnou', 'Coleman Wong',
                                                          'Aristotelis Thanos', 'Amr Elsayed Abdou Ahmed Mohamed',
                                                          'Rowland Phillips', 'Pavel Kotov', 'Gijs Brouwer',
                                                          'Manuel Guinard', 'Johan Nikles', 'Camilo Ugo Carabelli',
                                                          'Zdenek Kolar', 'Tim Van Rijthoven', 'Ryan Peniston']))

with col3:
    tournament = st.selectbox('tourney name', sorted(['Brisbane', 'Doha', 'Chennai', 'Sydney', 'Auckland',
                                                      'Australian Open', 'Santiago', 'Zagreb', 'Johannesburg',
                                                      'Rotterdam', 'San Jose',
                                                      'Costa Do Sauipe', 'Marseille', 'Memphis', 'Buenos Aires',
                                                      'Delray Beach',
                                                      'Dubai', 'Acapulco', 'Indian Wells Masters', 'Miami Masters',
                                                      'Houston',
                                                      'Casablanca', 'Monte Carlo Masters', 'Barcelona', 'Rome Masters',
                                                      'Munich',
                                                      'Estoril', 'Belgrade', 'Madrid Masters', 'Nice', 'Dusseldorf',
                                                      'Roland Garros', "Queen's Club", 'Halle', 's Hertogenbosch',
                                                      'Eastbourne',
                                                      'Wimbledon', 'Newport', 'Stuttgart', 'Bastad', 'Hamburg',
                                                      'Atlanta',
                                                      'Gstaad', 'Umag', 'Los Angeles', 'Washington', 'Canada Masters',
                                                      'Cincinnati Masters', 'New Haven', 'US Open', 'Metz', 'Bucharest',
                                                      'Kuala Lumpur', 'Bangkok', 'Tokyo', 'Beijing', 'Shanghai Masters',
                                                      'Stockholm', 'Moscow', 'Vienna', 'St. Petersburg', 'Montpellier',
                                                      'Valencia', 'Basel', 'Paris Masters', 'Tour Finals', 'Kitzbuhel',
                                                      'Winston-Salem', 'Sao Paulo', 'London Olympics', 'Bogota',
                                                      'Vina del Mar',
                                                      'Rio de Janeiro', 'Shenzhen', 'Quito', 'Istanbul', 'Geneva',
                                                      'Nottingham',
                                                      'Sofia', 'Marrakech', 'Rio Olympics', 'Los Cabos', 'Chengdu',
                                                      'Antwerp',
                                                      'NextGen Finals', 'Pune', 'New York', 'Cordoba', 'Zhuhai',
                                                      'Atp Cup',
                                                      'Adelaide', 'ATP Rio de Janeiro', 'Us Open', 'St Petersburg',
                                                      'Sardinia',
                                                      'Cologne 1', 'Cologne 2', 'Nur-Sultan', 'Murray River Open',
                                                      'Great Ocean Road Open', 'Singapore', 'Cagliari', 'Marbella',
                                                      'Parma',
                                                      'Belgrade 2', 'Mallorca', 'Tokyo Olympics', 'San Diego',
                                                      'Adelaide 1',
                                                      'Melbourne', 'Adelaide 2', 'Dallas', 'Belgrade ']))

col4, col5, col6 = st.columns(3)

with col4:
    surface = st.selectbox('surface', ['Hard', 'Clay', 'Carpet', 'Grass'])

with col5:
    round = st.selectbox('round', ['SF', 'F', 'QF', 'R16', 'R32', 'R64', 'R128', 'RR', 'BR'])

with col6:
    tourney_level = st.selectbox('tourney level', ['A', 'G', 'D', 'M', 'F'])

col7, col8, col9, col10 = st.columns(4)

with col7:
    first_player_hand = st.selectbox('first player hand', ['R', 'L', 'U'])

with col8:
    second_player_hand = st.selectbox('second player hand', ['R', 'L', 'U'])

with col9:
    winner_rank = st.number_input('first player rank', help='if the player is unranked than enter 0')

with col10:
    loser_rank = st.number_input('second player rank', help='if the player is unranked than enter 0')


col11, col12, col13, col14 = st.columns(4)

with col11:
    winner_ht = st.number_input('first player height', help='Put an integer')

with col12:
    loser_ht = st.number_input('second player height', help='Put an integer')

with col13:
    winner_age = st.number_input('first player age', help='Put an integer')

with col14:
    loser_age = st.number_input('second player age', help='Put an integer')


df.loc[len(df)] = [df['tourney_date'][len(df) - 1] + 1, tournament, surface, round, tourney_level, first_player_hand,
                   second_player_hand, winner_rank, loser_rank, winner_ht, loser_ht, winner_age, loser_age,
                   first_player, second_player]


def model(row, status, needed_data, classifier):
    list_of_predection = []  # la liste des prediction 1: pour un joueur qui gagne un match et
    # 0: pour un jour qui perd un match

    list_of_resultat = []  # liste des resultats du bookmaker

    player = df.loc[row][status]  # On selectione un joueur "winner" ou "Loser"

    df1 = df.iloc[0:row + 1]  # On selectionne un sous dataset qui contient toutes les informations du dataset
    # de 0 à row

    # On prend du df1 seulment les observations ou le joueur a joué
    df_player = df1[(df1['winner_name'] == player) | (df1['loser_name'] == player)].sort_values(by=['tourney_date'],
                                                                                                ascending=True)

    # on enlève la vairiables inutiles
    df_player = df_player.drop('tourney_date', axis=1)

    # On crée une colonne qui remplace le winner el le loser de chaque match par 1 et 0 respectivement.
    df_player['winner_name'] = df_player['winner_name'].replace(to_replace=player, value=1)
    df_player['loser_name'] = df_player['loser_name'].replace(to_replace=player, value=0)
    df_player['result'] = df_player.apply(lambda row: row['winner_name'] if type(row['winner_name']) == int
    else row['loser_name'], axis=1)

    # On supprime les colonnes Winner et loser qui ne sont plus utiles pour la suite
    df_player = df_player.drop(['winner_name', 'loser_name'], axis=1)
    df_player = df_player.dropna(axis=0, how='any')

    # On separe la variables cible des variables explicatives
    target = df_player['result']
    data = df_player.drop('result', axis=1)

    # on décode les variables qualitatives par la fonction get_dummies
    data = data.join(pd.get_dummies(data[['tourney_name', 'round', 'surface', 'tourney_level', 'round', 'winner_hand',
                                          'loser_hand']]))

    # On supprime les variables qualitatives
    data = data.drop(['tourney_name', 'round', 'surface', 'tourney_level', 'round', 'winner_hand', 'loser_hand'],
                     axis=1)

    if len(data) > needed_data:

        slice = int(len(data) * 0.75)
        for i in range(slice, len(data)):
            X_train = data.iloc[0:i]
            y_train = target.iloc[0:i]
            X_test = data.iloc[i:i + 1]
            y_test = np.array(target.iloc[i:i + 1])

            clf = classifier
            clf.fit(X_train, y_train)

            y_pred = clf.predict(X_test)
            list_of_predection.append(y_pred[0])
            list_of_resultat.append(y_test)


    else:

        return f'Not enough data for the {status} player {player}, Where the available informations are {len(data)} lines', 0, 0, 0, 0

    list = []  # cette liste contient les bon résultats de l'algorithme

    for value1, value2 in zip(list_of_predection, list_of_resultat):
        if value1 == value2:
            list.append(f'good predection')
        elif value1 != value2:
            list.append(f'bad predection')

    y_pred = clf.predict(data.tail(1))

    z = pd.DataFrame(list).value_counts(normalize=True)

    if y_pred[0] == 0:
        return f"avec un seuil de fidelité {z[0]} %", f"l'algorithme prédit que le joueur {player} va perdre le match et la prédiction est basée sur {len(data)} lignes"
    else:
        return f'avec un seuil de fidelité {z[0]} %', f"l'algorithme prédit que le joueur {player} va gagner le match et la prédiction est basée sur {len(data)} lignes"


KNN = neighbors.KNeighborsClassifier(n_neighbors=3, metric='minkowski', weights='distance')
Decision_tree = DecisionTreeClassifier(criterion='entropy', max_depth=20)
Random_forest = ensemble.RandomForestClassifier(criterion='entropy', max_depth=30, n_estimators=80)

classifier = st.selectbox('Choisir un classifier', ['KNN', 'Decision_tree', 'Random_forest'])

if classifier == 'KNN':
    a = model(row=len(df) - 1, status='winner_name', needed_data=30, classifier=KNN)
    b = model(row=len(df) - 1, status='loser_name', needed_data=30, classifier=KNN)
    st.write(a[1])
    st.write(a[0])
    st.write(b[1])
    st.write(b[0])

elif classifier == 'Decision_tree':
    a = model(row=len(df) - 1, status='winner_name', needed_data=30, classifier=Decision_tree)
    b = model(row=len(df) - 1, status='loser_name', needed_data=30, classifier=Decision_tree)
    st.write(a[1])
    st.write(a[0])
    st.write(b[1])
    st.write(b[0])

elif classifier == 'Random_forest':
    a = model(row=len(df) - 1, status='winner_name', needed_data=30, classifier=Random_forest)
    b = model(row=len(df) - 1, status='loser_name', needed_data=30, classifier=Random_forest)
    st.write(a[1])
    st.write(a[0])
    st.write(b[1])
    st.write(b[0])
