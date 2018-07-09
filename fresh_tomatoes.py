import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!--
author: W5layouts
author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!DOCTYPE html>
<html lang="en">
<head>
<title>Udacity Movies: an Entertainment Fullstack Project | Home :: w3layouts</title>
<!-- for-mobile-apps -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Udacity Movies: an Entertainment Fullstack Project" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false);
		function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- //for-mobile-apps -->
<link href="css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
<link rel="stylesheet" href="css/contactstyle.css" type="text/css" media="all" />
<link rel="stylesheet" href="css/faqstyle.css" type="text/css" media="all" />
<link href="css/single.css" rel='stylesheet' type='text/css' />
<link href="css/medile.css" rel='stylesheet' type='text/css' />
<!-- banner-slider -->
<link href="css/jquery.slidey.min.css" rel="stylesheet">
<!-- //banner-slider -->
<!-- pop-up -->
<link href="css/popuo-box.css" rel="stylesheet" type="text/css" media="all" />
<!-- //pop-up -->
<!-- font-awesome icons -->
<link rel="stylesheet" href="css/font-awesome.min.css" />
<!-- //font-awesome icons -->
<!-- js -->
<script type="text/javascript" src="js/jquery-2.1.4.min.js"></script>
<!-- //js -->
<!-- banner-bottom-plugin -->
<link href="css/owl.carousel.css" rel="stylesheet" type="text/css" media="all">
<script src="js/owl.carousel.js"></script>
<script>
	$(document).ready(function() {
		$("#owl-demo").owlCarousel({

		  autoPlay: 3000, //Set AutoPlay to 3 seconds

		  items : 5,
		  itemsDesktop : [640,4],
		  itemsDesktopSmall : [414,3]

		});

	});
</script>
<!-- //banner-bottom-plugin -->
<link href='//fonts.googleapis.com/css?family=Roboto+Condensed:400,700italic,700,400italic,300italic,300' rel='stylesheet' type='text/css'>
<!-- start-smoth-scrolling -->
<script type="text/javascript" src="js/move-top.js"></script>
<script type="text/javascript" src="js/easing.js"></script>
<script type="text/javascript">
	jQuery(document).ready(function($) {
		$(".scroll").click(function(event){
			event.preventDefault();
			$('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
		});
	});
</script>
<!-- start-smoth-scrolling -->
</head>
'''

# The main page layout and title bar
main_page_content = '''
<body>
<!-- header -->
	<div class="header">
		<div class="container">
			<div class="w3layouts_logo">
				<a href="index.html"><h1>Udacity<span>Movies</span></h1></a>
			</div>
			<div class="clearfix"> </div>
		</div>
	</div>
<!-- //header -->
<!-- nav -->
	<div class="movies_nav">
		<div class="container">
			<nav class="navbar navbar-default">
				<div class="navbar-header navbar-left">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
				</div>
				<!-- Collect the nav links, forms, and other content for toggling -->
				<div class="collapse navbar-collapse navbar-right" id="bs-example-navbar-collapse-1">
					<nav>
						<ul class="nav navbar-nav">
							<li class="active"><a href="index.html">Home</a></li>
						</ul>
					</nav>
				</div>
			</nav>
		</div>
	</div>
<!-- //nav -->
<!-- banner -->
	<div id="slidey" style="display:none;">
		<ul>{first_slider_content}
		</ul>
  </div>
    <script src="js/jquery.slidey.js"></script>
    <script src="js/jquery.dotdotdot.min.js"></script>
	   <script type="text/javascript">
			$("#slidey").slidey({{
				interval: 8000,
				listCount: 5,
				autoplay: false,
				showList: true
			}});
			$(".slidey-list-description").dotdotdot();
		</script>
<!-- banner-bottom -->
	<div class="banner-bottom">
		<div class="container">
			<div class="w3_agile_banner_bottom_grid">
				<div id="owl-demo" class="owl-carousel owl-theme">
					{second_slider_content}
				</div>
			</div>
		</div>
	</div>
<!-- //banner-bottom -->
<div class="general_social_icons">
	<nav class="social">
		<ul>
			<li class="w3_twitter"><a href="#">Twitter <i class="fa fa-twitter"></i></a></li>
			<li class="w3_facebook"><a href="#">Facebook <i class="fa fa-facebook"></i></a></li>
			<li class="w3_g_plus"><a href="#">Google+ <i class="fa fa-google-plus"></i></a></li>
		</ul>
  </nav>
</div>
<!-- general -->
	<div class="general">
		<h4 class="latest-text w3_latest_text">Featured Movies</h4>
		<div class="container">
			<div class="bs-example bs-example-tabs" role="tabpanel" data-example-id="togglable-tabs">
				<ul id="myTab" class="nav nav-tabs" role="tablist">
					<li role="presentation" class="active"><a href="#home" id="home-tab" role="tab" data-toggle="tab" aria-controls="home" aria-expanded="true">Featured</a></li>
					<li role="presentation"><a href="#profile" role="tab" id="profile-tab" data-toggle="tab" aria-controls="profile" aria-expanded="false">Top viewed</a></li>
					<li role="presentation"><a href="#rating" id="rating-tab" role="tab" data-toggle="tab" aria-controls="rating" aria-expanded="true">Top Rating</a></li>
					<li role="presentation"><a href="#imdb" role="tab" id="imdb-tab" data-toggle="tab" aria-controls="imdb" aria-expanded="false">Recently Added</a></li>
				</ul>
				<div id="myTabContent" class="tab-content">
					<div role="tabpanel" class="tab-pane fade active in" id="home" aria-labelledby="home-tab">
						<div class="w3_agile_featured_movies">
							{featured_content}
							<div class="clearfix"> </div>
						</div>
					</div>
					<div role="tabpanel" class="tab-pane fade" id="profile" aria-labelledby="profile-tab">
					    {top_viewed_content}
						<div class="clearfix"> </div>
					</div>
					<div role="tabpanel" class="tab-pane fade" id="rating" aria-labelledby="rating-tab">
					    {top_rated_content}
						<div class="clearfix"> </div>
					</div>
					<div role="tabpanel" class="tab-pane fade" id="imdb" aria-labelledby="imdb-tab">
						  {recently_added_content}
						<div class="clearfix"> </div>
					</div>
				</div>
			</div>
		</div>
	</div>
<!-- //general -->
<script src="js/bootstrap.min.js"></script>
<!-- pop-up-box -->
<script src="js/jquery.magnific-popup.js" type="text/javascript"></script>
<!--//pop-up-box -->
{pop_up_content}
	<script>
		$(document).ready(function() {{
		$('.w3_play_icon,.w3_play_icon1,.w3_play_icon2').magnificPopup({{
			type: 'inline',
			fixedContentPos: false,
			fixedBgPos: true,
			overflowY: 'auto',
			closeBtnInside: true,
			preloader: false,
			midClick: true,
			removalDelay: 300,
			mainClass: 'my-mfp-zoom-in'
		}});

	}});
	</script>
<!-- footer -->
<div class="footer">
		<div class="container">
			<div class="col-md-5 w3ls_footer_grid1_left">
				<p>&copy; 2018 Udacity Movies. All rights reserved</p>
				<p>Design by <a href="http://w3layouts.com/">W3layouts</a></p>
			</div>
			<div class="clearfix"> </div>
		</div>
	</div>
<!-- //footer -->
<!-- here stars scrolling icon -->
	<script type="text/javascript">
		$(document).ready(function() {{

			$().UItoTop({{ easingType: 'easeOutQuart' }});

		}});
	</script>
<!-- //here ends scrolling icon -->
</body>
</html>
'''

# A single movie entry for the first slider: html template
first_slider_content = '''
<li><img src="{poster_image_url}" alt=" "><p class='title'>{movie_title}</p><p class='description'>{movie_description}</p></li>'''
pop_up_content = '''
	<div id="{video_id}" class="mfp-hide">
		 <iframe src="https://www.youtube.com/embed/{video_id}">
</iframe>
	</div>
'''

# A single movie entry for the second slider: html template
second_slider_content = '''
<div class="item">
  <div class="w3l-movie-gride-agile w3l-movie-gride-agile1">
        <a href="#{video_id}" class="w3_play_icon hvr-shutter-out-horizontal"><img src="{poster_image_url}" title="{movie_description}" class="img-responsive" alt=""/>
            <div class="w3l-action-icon"><i class="fa fa-play-circle" aria-hidden="true"></i></div>
        </a>
        <div class="mid-1 agileits_w3layouts_mid_1_home">
            <div class="w3l-movie-text">
                <h6>{movie_title}</h6>
            </div>
            <div class="mid-2 agile_mid_2_home">
                <p>{movie_release}</p>
                <div class="block-stars">
                    <ul class="w3l-ratings">
                        {movie_rating}
                    </ul>
                </div>
                <div class="clearfix"></div>
            </div>
        </div>
        <div class="ribben">
            <p>NEW</p>
        </div>
    </div>
  </div>
'''
# A single movie entry for the featured,Top Rating,Top Viewed,Recently Added section: html template
top_content = '''<div class="col-md-2 w3l-movie-gride-agile">
                        <a href="#{video_id}" class="w3_play_icon hvr-shutter-out-horizontal"><img src="{poster_image_url}" title="{movie_description}" class="img-responsive" alt="" />
                            <div class="w3l-action-icon"><i class="fa fa-play-circle" aria-hidden="true"></i></div>
                        </a>
                        <div class="mid-1 agileits_w3layouts_mid_1_home">
                            <div class="w3l-movie-text">
                                <h6>{movie_title}</h6>
                            </div>
                            <div class="mid-2 agile_mid_2_home">
                                <p>{movie_release}</p>
                                <div class="block-stars">
                                    <ul class="w3l-ratings">
                                       {movie_rating}
                                    </ul>
                                </div>
                                <div class="clearfix"></div>
                            </div>
                        </div>
                        <div class="ribben">
                            <p>NEW</p>
                        </div>
                    </div>'''


# Generate the popups for the trailers
def create_pop_ups(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        # Append the tile for the movie with its content filled in
        content += pop_up_content.format(
            video_id=trailer_youtube_id)
    return content


# Generate the first slider elements
def create_first_slider_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += first_slider_content.format(
            movie_title=movie.title,
            poster_image_url=movie.thumbnail,
            movie_description=movie.storyline
        )
    return content


# Generate the second slider elements
def create_second_slider_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += second_slider_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            video_id=trailer_youtube_id,
            movie_release=movie.release_date,
            movie_description=movie.storyline,
            movie_rating=generate_rating(movie.rating)
        )
    return content


# Generate the featured section elements
def create_top_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Generate  Movie rating

        # Append the tile for the movie with its content filled in
        content += top_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            video_id=trailer_youtube_id,
            movie_release=movie.release_date,
            movie_description=movie.storyline,
            movie_rating=generate_rating(movie.rating).strip()
        )
    return content


# Generate the rating for each movie
def generate_rating(rating):
    # The HTML content for this section of the page
    content = ''
    star = '''<li><a href="#"><i class="fa fa-star" aria-hidden="true"></i></a></li>'''
    half_star = '''<li><a href="#"><i class="fa fa-star-half-o" aria-hidden="true"></i></a></li>'''
    no_star = '''	<li><a href="#"><i class="fa fa-star-o" aria-hidden="true"></i></a></li>'''
    for x in range(5):
        if x < int(rating):
            content += star.strip()
        elif x == int(rating) and not isinstance(rating, int):
            content += half_star.strip()
        else:
            content += no_star.strip()

    return content


# Create the index based on the templates
def open_movies_page(movies, fs_movies, ss_movies, feat_movies, topv_movies, topr_movies, ra_movies):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the  placeholders in the body with generated content
    rendered_content = main_page_content.format(
        first_slider_content=create_first_slider_content(fs_movies),
        second_slider_content=create_second_slider_content(ss_movies),
        featured_content=create_top_content(feat_movies),
        top_viewed_content=create_top_content(topv_movies),
        top_rated_content=create_top_content(topr_movies),
        recently_added_content=create_top_content(ra_movies),
        pop_up_content=create_pop_ups(movies)
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
