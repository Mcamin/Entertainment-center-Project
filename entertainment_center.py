import media
import fresh_tomatoes


# Instances of Movie Class
citizen_soldier = media.Movie("Citizen Soldier",
                              "CITIZEN SOLDIER is a dramatic feature film, told from the point of view of a group of "
                              "Soldiers "
                              "in the Oklahoma Army National Guard's 45th Infantry Brigade Combat Team, known since "
                              "World "
                              "War... ",
                              "images/m13.jpg", "", "https://www.youtube.com/watch?v=-d-BcfRGl7c", 2, "2016")

greater = media.Movie("Greater",
                      "Greater is a movie starring Neal McDonough, Leslie Easterbrook, and Christopher Severio. The "
                      "story of Brandon Burlsworth, possibly the greatest walk-on in the history of college football.",
                      "images/m12.jpg", "", "https://www.youtube.com/watch?v=v0Ow6lhvPNk", 3.5, "2016")

light_between_ocean = media.Movie("The Light Between Oceans",
                                  "A lighthouse keeper and his wife living off the coast of Western Australia raise a "
                                  "baby they rescue from a drifting rowing boat.",
                                  "images/m7.jpg", "", "https://www.youtube.com/watch?v=YSX-mpsVutQ", 3, "2016")

thebfg = media.Movie("The BFG",
                     "An orphan little girl befriends a benevolent giant who takes her to Giant Country, where they "
                     "attempt to stop the man-eating giants that are invading the human world.",
                     "images/m8.jpg", "", "https://www.youtube.com/watch?v=GZ0Bey4YUGI", 3, "2016")

Dont_think_twice = media.Movie("Don't Think Twice",
                               "When a member of a popular New York City improv troupe gets a huge break, the rest of "
                               "the group - all best friends - start to realize that not everyone is going to make it "
                               "after all. ",
                               "images/m10.jpg", "", "https://www.youtube.com/watch?v=9RFTpObS95U", 3.5, "2016")

peter = media.Movie("The Apostle Peter: Redemption",
                    "Tormented by his denial of Christ, Peter spent his life attempting to atone for his failures. "
                    "Now as he faces certain death at the hand of Nero, will he falter again, his weakness betray ...",
                    "images/m17.jpg", "", "https://www.youtube.com/watch?v=43aUvmQw55Q", 3, "2016")

god_s_compass = media.Movie("God's Compass",
                            "On the night Suzanne Waters celebrates her retirement, she is faced with a series of "
                            "crisis she could not have imagined.",
                            "images/m15.jpg", "", "https://www.youtube.com/watch?v=qLtD4orE2r4", 4.5, "2016")

badmoms = media.Movie("Bad Moms",
                      "When three overworked and under-appreciated moms are pushed beyond their limits, they ditch "
                      "their conventional responsibilities for a jolt of long overdue freedom, fun, and comedic "
                      "self-indulgence.",
                      "images/m2.jpg", "", "https://www.youtube.com/watch?v=iKCw-kqo3cs", 2.5, "2016")

tarzan = media.Movie("The Legend of Tarzan",
                     "Tarzan, having acclimated to life in London, is called back to his former "
                     "home in the jungle to investigate the activities at a mining encampment.", "images/m3.jpg",
                     "images/5.jpg", "https://www.youtube.com/watch?v=91rm_G1xkU8", 3, "2016")

maximum_ride = media.Movie("Maximum Ride",
                           "Six children, genetically cross-bred with avian DNA, take flight around the "
                           "country to discover their origins. Along the way, their mysterious past is "
                           "...", "images/m1.jpg", "images/2.jpg", "https://www.youtube.com/watch?v=lhQiwVi3jdo", 2,
                           "2016")

independence = media.Movie("Independence Day: Resurgence", "The fate of humanity hangs in the balance as the U.S. "
                                                           "President and citizens decide if these aliens are to be "
                                                           "trusted ...or feared.", "images/m14.jpg", "images/3.jpg",
                           "https://www.youtube.com/watch?v=LbduDRH2m2M", 2.5, "2016")

central_intelligence = media.Movie("Central Intelligence", "Bullied as a teen for being overweight, Bob Stone (Dwayne "
                                                           "Johnson) shows up to his high school reunion looking fit "
                                                           "and muscular. Claiming to be on a top-secret ...",
                                   "images/m9.jpg",
                                   "images/4.jpg",
                                   "https://www.youtube.com/watch?v=MxEw3elSJ8M", 3.5, "2016")

ice_age = media.Movie("Ice Age: Collision Course",
                      "In the film's epilogue, Scrat keeps struggling to control the alien "
                      "ship until it crashes on Mars, destroying all life on the planet.", "images/m22.jpg",
                      "images/6.jpg", "https://www.youtube.com/watch?v=HyLquKn3Swc", 3, "2016")

x_men = media.Movie("X-Men: Apocalypse",
                    "In 1977, paranormal investigators Ed (Patrick Wilson) and Lorraine Warren come "
                    "out of a self-imposed sabbatical to travel to Enfield, a borough in north "
                    "...", "images/m11.jpg", "images/1.jpg", "https://www.youtube.com/watch?v=Jer8XjMrUB4", 3.5, "2016")


# All Movies List :to generate the trailer links
Movies = [citizen_soldier, peter, greater, light_between_ocean, Dont_think_twice, god_s_compass, thebfg,
          central_intelligence, x_men, tarzan, maximum_ride, independence, central_intelligence, ice_age, x_men]

# First slider list
Slider_1 = [tarzan, maximum_ride, independence, central_intelligence, ice_age, x_men]

# Second slider list
Slider_2 = [citizen_soldier, peter, greater, light_between_ocean, Dont_think_twice, god_s_compass, thebfg,
            central_intelligence, x_men]

# Featured List
Slider_3 = [citizen_soldier, Dont_think_twice, god_s_compass, thebfg,
            central_intelligence, x_men, tarzan, maximum_ride, independence, central_intelligence, ice_age, x_men]

# Top Viewed List
Slider_4 = [peter, greater, light_between_ocean, Dont_think_twice]

# Top Rated List
Slider_5 = [badmoms, Dont_think_twice, central_intelligence, x_men, ice_age]

# Recently Added List
Slider_6 = [peter, independence, maximum_ride, thebfg]

# call of the open_movie_page to create the index file and generate page content
fresh_tomatoes.open_movies_page(Movies, Slider_1, Slider_2, Slider_3, Slider_4, Slider_5,
                                Slider_6)
