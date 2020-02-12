# Содержит списки с вложенными списками тегов 
# 1 элемент - тег в сыром формате 
# 2 элемент - символ замены


title = [[r"<title>", ""], [r"</title>", ""], [r"\t", ""], [r"\n", ""],
        [r" — Блог Гродно s13", ""], [r" - NewGrodno.By", ""], [r" :: Гродненская правда", ""], 
        [r" — Новости — Новости и события Гродно", ""], 
        [r"Гродно Плюс. Новости Гродно. Телевидение Гродно. Официальный сайт - ", ""]]

content = [[r"\t", ""], [r"\r", ""], [r"<a .*?>", ""], [r"\n", ""],
        [r"</a>", ""], [r"<img .*?>", ""], [r"<p>Поделиться:</p>", ""], 
        [r"Поделись с друзьями", ""], [r"Популярныеновости", ""], [r"<hr.*?hr/>", ""], 
        [r"<p>", ""], [r"<p.*?>", ""], 
        [r"</p>", "\n"], [r"<i>", ""], [r"</i>", ""], 
        [r"<h2>", ""], [r"</h2>", ""], [r"<strong>", ""], 
        [r"</strong>", ""], [r"<blockquote>", ""], [r"</blockquote>", ""], 
        [r"<iframe .*?</iframe>", ""], [r"<h13>", ""], [r"</h13>", ""], 
        [r"<em>", ""], [r"</em>", ""], [r"<span .*?>", ""], 
        [r"</span>", ""], [r"<br.*?/>", "\n"], [r"\u2212", "-"], 
        [r"<script .*?</script>", ""], [r"<h1>.*?</h1>", ""], [r"</img>", ""], 
        [r"<b>", ""], [r"</b>", ""], [r"<date>.*?<date>", ""], 
        [r"</date>", ""], [r"<br/>", "\n"],[r"<div.*?>", ""], 
        [r"</div>", ""],  [r"\n+?\n", "\n"],
        [r"\u2009", ""], [r"<.*?>", ""], [r"-->", ""]]