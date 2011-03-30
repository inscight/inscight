"""Posts an episode of inSCIght to the intarnets."""


import pyblog
import passwd



def post_to_wordpress(post):
    """Posts an episode to sciencepodcasters.org.  Takes a dictionary
    post to do this.
    """
    un = passwd.WORDPRESS_USERNAME
    pw = passwd.WORDPRESS_PASSWORD
    wp = pyblog.WordPress("http://inscight.org/xmlrpc.php", un, pw)
    print wp.get_post(84)['title']


def post_to_sciencepodcasters(post):
    """Posts an episode to sciencepodcasters.org.  Takes a dictionary
    post to do this.
    """
    un = "http://sciencepodcasters.squarespace.com/" + passwd.SCIENCEPODCASTERS_USERNAME
    pw = passwd.SCIENCEPODCASTERS_PASSWORD
    sp = pyblog.MetaWeblog("http://www.squarespace.com/process/service/PostInterceptor", un, pw)




def main():
    post_to_wordpress(None)
    post_to_sciencepodcasters(None)


if __name__ == "__main__":
    main()
