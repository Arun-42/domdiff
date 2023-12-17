prompts = [
    """
You are a dom-differ. You will be provided two html documents, one "initial-html", and one "post-html". When some dynamic change has been made to the initial page, the post page is reached, giving post html.

Example: the event could be the clicking of a sidebar button, and thus the diff will contain addition of sidebar and some list of items. In such case you should summarize the changes like: 
1. sidebar is now visible
2. sidebar contains a three new links to different parts of the article
3. the links include: heading, sub heading 1, sub heading 2, conclusion

Do not mention changes to specific tags, or classes or anything to indicate html. Your answer should be equivalent to someone using the website with just the GUI. Interpret the visual changes to be best of your ability from html, and describe it as such. Do not mention super specific details. Be general. 
    """,
    """
You are a dom-differ. You will be provided a diff of two html documents, one "initial-html", and one "post-html". When some dynamic change has been made to the initial page, the post page is reached, giving post html. You are given the diff of the two htmls.

Example: the event could be the clicking of a sidebar button, and thus the diff will contain addition of sidebar and some list of items. In such case you should summarize the changes like: 
1. sidebar is now visible
2. sidebar contains a three new links to different parts of the article
3. the links include: heading, sub heading 1, sub heading 2, conclusion

Do not mention changes to specific tags, or classes or anything to indicate html. Your answer should be equivalent to someone using the website with just the GUI. Interpret the visual changes to be best of your ability from html, and describe it as such. Do not mention super specific details. Be general. 
NOTE: focus only on the lines that are modifyed. Modifications are indicated using standard diff notation: (-) for delete, (+) for insert
    """,
]

diffs = [
    """
    --- a/initial.html                                                                                                                                                                           
+++ b/post.html                                                                                                                                                                              
@@ -1,48 +1,62 @@                                                                                                                                                                            
 <body>                                                                                                                                                                                      
     <header>                                                                                                                                                                                
       <h1 class="home"><a href="/">                                                                                                                                                         
       <img id="logo" src="https://cdn.glitch.com/33ee6b19-10fa-4d51-8898-d35eb670b3fe%2Fbatlab150-FINAL-inv.png?v=1600125915264" alt="Batlab Electronics logo"></img></a></h1>              
       <ul class="nav">                                                                                                                                                                      
       <li class="nav-item">                                                                                                                                                                 
         <a href="/">Home</a>                                                                                                                                                                
       </li>                                                                                                                                                                                 
         <li class="nav-item">                                                                                                                                                               
           <ul class="projects-tag-list">                                                                                                                                                    
             <li class="projects-tag">                                                                                                                                                       
               <button class="tag-header-button"><span class="toggle">+</span> NES</button>                                                                                                  
             </li>                                                                                                                                                                                                                          
             <li class="projects-tag">
               <button class="tag-header-button"><span class="toggle">+</span> SEGA</button>                                                                                                 
             </li>                                                                                                                                                                                                
             <li class="projects-tag">                                                                                                 
               <button class="tag-header-button"><span class="toggle">+</span> Visuals</button>                                                                                                                                                                               
             </li>                                                                                                                                                                                                
             <li class="projects-tag">                                                                                                                                                                                                                                        
-              <button class="tag-header-button"><span class="toggle">+</span> Web</button>                                            
+              <button class="tag-header-button"><span class="toggle">-</span> Web</button>                                                                                                  
+              <ul class="tag-posts-list collapsed">                                                                                   
+                    <li class="postlist-item">                                                                                                                                                                   
+                      <a href="/posts/telesplit/" class="postlist-link  nav-item-active">Telesplit</a>                                                                                                                                                                       
+                    </li>                                                                                                                                                                                                                                                    
+                    <li class="postlist-item">                                                                                                                                                                                             
+                      <a href="/posts/telemelt/" class="postlist-link ">Telemelt</a>                                                                                                        
+                    </li>                                                                                                                                                                                                                                                    
+                    <li class="postlist-item">
+                      <a href="/posts/telesplit-2017/" class="postlist-link ">Telesplit (2017)</a>                                                                                          
+                    </li>                                                                               
+                    <li class="postlist-item">
+                      <a href="/posts/the-end-society/" class="postlist-link ">The End Society</a>                                                                                                                                                                           
+                    </li>                                                                                            
+              </ul>                                                                                                                                                                         
             </li>                                                                                                                                                                                                
             <li class="projects-tag">                                                                   
               <button class="tag-header-button"><span class="toggle">+</span> Electronics</button>                                                                                                               
             </li>                                                                                                                                                                                                
         </ul>                                                                                                                                                                                                    
       </li>                                                                                                                                                                                                                                
       <li class="nav-item">                                                                                                                                                                                                                
         <a href="/about/">About</a>                                                                                                                                                                                                        
       </li>                  
 </ul>                                                                                                                                                                                                                                                                        
       <p id="copyright">Copyright _ 2022 Andrew Reitano; All rights reserved.</p>                                                                                                                                                                                            
     </header>                                                                                                                         
     <main class="tmpl-post">                                                                                                                                                                                                                                                 
       <h1>Telesplit</h1>                                                                                                                                                                                                                                                     
 <p>Telesplit is designed to quickly extract samples from VGM files for game audio research and isolating individual channels for musicians that perform live covers/remixes.<br></br>                                                                                        
 Featuring fast decoding using wasm and a fun mini-DAW for live playback/waveform slicing.</p>                                                                                                                                                                                
 <p><a href="https://telesplit.com">telesplit.com</a></p>                                                                              
 <p>Try loading one of your favorite tracks and muting individual channels using right-click or 1-8 on the keyboard!<br></br>                                                                                                                                                 
 All processing is done in browser memory - no more stale .wav files clogging up your hard drive to get that perfect sample.</p>                                                                                                                                              
 <p><img src="https://cdn.glitch.global/33ee6b19-10fa-4d51-8898-d35eb670b3fe/54e3e68c-c106-47f5-a810-8652f0a95e0f.image.png?v=1659151275891"></img></p>                                                                                                                       
 <p><a href="/">_ Home</a></p>                                     
     </main>                                                       
     <#comment></#comment>                                         
     <footer>                                                      
     </footer>                                                     
 </body>
"""
]

h0 = [("""
<body>
    <header>
      <h1 class="home"><a href="/">
      <img id="logo" src="https://cdn.glitch.com/33ee6b19-10fa-4d51-8898-d35eb670b3fe%2Fbatlab150-FINAL-inv.png?v=1600125915264" alt="Batlab Electronics logo"></img></a></h1>
      <ul class="nav">
      <li class="nav-item">
        <a href="/">Home</a>
      </li>
        <li class="nav-item">
          <ul class="projects-tag-list">
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">+</span> NES</button>
            </li>
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">+</span> SEGA</button>
            </li>
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">+</span> Visuals</button>
            </li>
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">-</span> Web</button>
              <ul class="tag-posts-list collapsed">
                    <li class="postlist-item">
                      <a href="/posts/telesplit/" class="postlist-link  nav-item-active">Telesplit</a>
                    </li>
                    <li class="postlist-item">
                      <a href="/posts/telemelt/" class="postlist-link ">Telemelt</a>
                    </li>
                    <li class="postlist-item">
                      <a href="/posts/telesplit-2017/" class="postlist-link ">Telesplit (2017)</a>
                    </li>
                    <li class="postlist-item">
                      <a href="/posts/the-end-society/" class="postlist-link ">The End Society</a>
                    </li>
              </ul>
            </li>
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">+</span> Electronics</button>
            </li>
        </ul>
      </li>
      <li class="nav-item">
        <a href="/about/">About</a>
      </li>
</ul>
      <p id="copyright">Copyright © 2022 Andrew Reitano; All rights reserved.</p>
    </header>
    <main class="tmpl-post">
      <h1>Telesplit</h1>
<p>Telesplit is designed to quickly extract samples from VGM files for game audio research and isolating individual channels for musicians that perform live covers/remixes.<br></br>
Featuring fast decoding using wasm and a fun mini-DAW for live playback/waveform slicing.</p>
<p><a href="https://telesplit.com">telesplit.com</a></p>
<p>Try loading one of your favorite tracks and muting individual channels using right-click or 1-8 on the keyboard!<br></br>
All processing is done in browser memory - no more stale .wav files clogging up your hard drive to get that perfect sample.</p>
<p><img src="https://cdn.glitch.global/33ee6b19-10fa-4d51-8898-d35eb670b3fe/54e3e68c-c106-47f5-a810-8652f0a95e0f.image.png?v=1659151275891"></img></p>
<p><a href="/">← Home</a></p>
    </main>
    <#comment></#comment>
    <footer>
    </footer>
<button style="position: fixed; top: 10px; right: 10px; z-index: 999;">Run Me</button>
</body>
""",
"""
<body>
    <header>
      <h1 class="home"><a href="/">
      <img id="logo" src="https://cdn.glitch.com/33ee6b19-10fa-4d51-8898-d35eb670b3fe%2Fbatlab150-FINAL-inv.png?v=1600125915264" alt="Batlab Electronics logo"></img></a></h1>
      <ul class="nav">
      <li class="nav-item">
        <a href="/">Home</a>
      </li>
        <li class="nav-item">
          <ul class="projects-tag-list">
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">+</span> NES</button>
            </li>
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">-</span> SEGA</button>
              <ul class="tag-posts-list collapsed">
                    <li class="postlist-item">
                      <a href="/posts/genesis-spectrum-analyzer/" class="postlist-link ">Genesis Spectrum Analyzer</a>
                    </li>
                    <li class="postlist-item">
                      <a href="/posts/genesis-flashcarts/" class="postlist-link ">Genesis Flashcarts</a>
                    </li>
                    <li class="postlist-item">
                      <a href="/posts/color-mechanica/" class="postlist-link ">Color Mechanica</a>
                    </li>
              </ul>
            </li>
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">+</span> Visuals</button>
            </li>
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">-</span> Web</button>
              <ul class="tag-posts-list collapsed">
                    <li class="postlist-item">
                      <a href="/posts/telesplit/" class="postlist-link  nav-item-active">Telesplit</a>
                    </li>
                    <li class="postlist-item">
                      <a href="/posts/telemelt/" class="postlist-link ">Telemelt</a>
                    </li>
                    <li class="postlist-item">
                      <a href="/posts/telesplit-2017/" class="postlist-link ">Telesplit (2017)</a>
                    </li>
                    <li class="postlist-item">
                      <a href="/posts/the-end-society/" class="postlist-link ">The End Society</a>
                    </li>
              </ul>
            </li>
            <li class="projects-tag">
              <button class="tag-header-button"><span class="toggle">+</span> Electronics</button>
            </li>
        </ul>
      </li>
      <li class="nav-item">
        <a href="/about/">About</a>
      </li>
</ul>
      <p id="copyright">Copyright © 2022 Andrew Reitano; All rights reserved.</p>
    </header>
    <main class="tmpl-post">
      <h1>Telesplit</h1>
<p>Telesplit is designed to quickly extract samples from VGM files for game audio research and isolating individual channels for musicians that perform live covers/remixes.<br></br>
Featuring fast decoding using wasm and a fun mini-DAW for live playback/waveform slicing.</p>
<p><a href="https://telesplit.com">telesplit.com</a></p>
<p>Try loading one of your favorite tracks and muting individual channels using right-click or 1-8 on the keyboard!<br></br>
All processing is done in browser memory - no more stale .wav files clogging up your hard drive to get that perfect sample.</p>
<p><img src="https://cdn.glitch.global/33ee6b19-10fa-4d51-8898-d35eb670b3fe/54e3e68c-c106-47f5-a810-8652f0a95e0f.image.png?v=1659151275891"></img></p>
<p><a href="/">← Home</a></p>
    </main>
    <#comment></#comment>
    <footer>
    </footer>
<button style="position: fixed; top: 10px; right: 10px; z-index: 999;">Run Me</button>
</body>
"""), 
(
"""
<body dir="ltr">
  <main class="container flex">
    <aside class="book-menu">
      <div class="book-menu-content">
  <nav>
<h2 class="book-brand">
  <a class="flex align-center" href="/"><span>Hugo Book</span>
  </a>
</h2>
<div class="book-search">
  <input type="text" id="book-search-input" placeholder="Search" aria-label="Search" maxlength="64" data-hotkeys="s/"></input>
  <ul id="book-search-results"></ul>
</div>
<ul class="book-languages">
  <li>
    <input type="checkbox" id="languages" class="toggle"></input>
    <label for="languages" class="flex justify-between">
      <a role="button" class="flex align-center">
        <img src="/svg/translate.svg" class="book-icon" alt="Languages"></img>
        English
      </a>
    </label>
  </li>
</ul>
  <ul>
        <li class="book-section-flat">
    <a href="/docs/example/">Example Site</a>
  <ul>
        <li>
    <a href="/docs/example/table-of-contents/">Table of Contents</a>
  <ul>
        <li>
    <a href="/docs/example/table-of-contents/with-toc/">With ToC</a>
        </li>
        <li>
    <a href="/docs/example/table-of-contents/without-toc/">Without ToC</a>
        </li>
  </ul>
        </li>
        <li>
    <input type="checkbox" id="section-4e46b01272d410b3a99461d79326ddf4" class="toggle"></input>
    <label for="section-4e46b01272d410b3a99461d79326ddf4" class="flex justify-between">
      <a role="button">Collapsed</a>
    </label>
        </li>
  </ul>
        </li>
        <li class="book-section-flat">
    <span>Shortcodes</span>
  <ul>
        <li>
    <a href="/docs/shortcodes/buttons/">Buttons</a>
        </li>
        <li>
    <a href="/docs/shortcodes/columns/">Columns</a>
        </li>
        <li>
    <a href="/docs/shortcodes/details/">Details</a>
        </li>
        <li>
    <a href="/docs/shortcodes/expand/">Expand</a>
        </li>
        <li>
    <a href="/docs/shortcodes/hints/">Hints</a>
        </li>
        <li>
    <a href="/docs/shortcodes/katex/">Katex</a>
        </li>
        <li>
    <a href="/docs/shortcodes/mermaid/">Mermaid</a>
        </li>
        <li>
    <input type="checkbox" id="section-d3fc1bf6d66cd84b896a0af9f40cb1d5" class="toggle"></input>
    <label for="section-d3fc1bf6d66cd84b896a0af9f40cb1d5" class="flex justify-between">
      <a href="/docs/shortcodes/section/">Section</a>
    </label>
        </li>
        <li>
    <a href="/docs/shortcodes/tabs/">Tabs</a>
        </li>
  </ul>
        </li>
  </ul>
<ul>
  <li>
    <a href="/posts/">
        Blog
      </a>
  </li>
  <li>
    <a href="https://github.com/alex-shpak/hugo-book" target="_blank" rel="noopener">
        Github
      </a>
  </li>
  <li>
    <a href="https://themes.gohugo.io/hugo-book/" target="_blank" rel="noopener">
        Hugo Themes
      </a>
  </li>
</ul>
</nav>
      </div>
    </aside>
    <div class="book-page">
  <article class="markdown"><h1 id="acerbo-datus-maxime">
  Acerbo datus maxime
  <a class="anchor" href="#acerbo-datus-maxime">#</a>
</h1>
<div class="book-columns flex flex-wrap">
  <div class="flex-even markdown-inner">
    <h2 id="astris-ipse-furtiva">
  Astris ipse furtiva
  <a class="anchor" href="#astris-ipse-furtiva">#</a>
</h2>
<p>Est in vagis et Pittheus tu arge accipiter regia iram vocatur nurus. Omnes ut
olivae sensit <strong>arma sorori</strong> deducit, inesset <strong>crudus</strong>, ego vetuere aliis,
modo arsit? Utinam rapta fiducia valuere litora <em>adicit cursu</em>, ad facies
  </p></div>
  <div class="flex-even markdown-inner">
    <h2 id="suis-quot-vota">
  Suis quot vota
  <a class="anchor" href="#suis-quot-vota">#</a>
</h2>
<p>Ea <em>furtique</em> risere fratres edidit terrae magis. Colla tam mihi tenebat:
miseram excita suadent es pecudes iam. Concilio <em>quam</em> velatus posset ait quod
nunc! Fragosis suae dextra geruntur functus vulgata.
  </p></div>
</div>
<h2 id="tempora-nisi-nunc">
  Tempora nisi nunc
  <a class="anchor" href="#tempora-nisi-nunc">#</a>
</h2>
<p>Lorem <strong>markdownum</strong> emicat gestu. Cannis sol pressit ducta. <strong>Est</strong> Idaei,
tremens ausim se tutaeque, illi ulnis hausit, sed, lumina cutem. Quae avis
sequens!</p>
<pre><code>var panel = ram_design;
if (backup + system) {
    file.readPoint = network_native;
    sidebar_engine_device(cell_tftp_raster,
            dual_login_paper.adf_vci.application_reader_design(
            graphicsNvramCdma, lpi_footer_snmp, integer_model));
}
</code></pre>
<h2 id="locis-suis-novi-cum-suoque-decidit-eadem">
  Locis suis novi cum suoque decidit eadem
  <a class="anchor" href="#locis-suis-novi-cum-suoque-decidit-eadem">#</a>
</h2>
<p>Idmoniae ripis, at aves, ali missa adest, ut <em>et autem</em>, et ab?</p>
</article>
      <footer class="book-footer">
  <div class="flex flex-wrap justify-between">
  <div><a class="flex align-center" href="https://github.com/alex-shpak/hugo-book/commit/9013a1f4570885416254aabbe7e389822d2fb215" title="Last modified by Alex Shpak | November 2, 2022" target="_blank" rel="noopener">
      <img src="/svg/calendar.svg" class="book-icon" alt="Calendar"></img>
      <span>November 2, 2022</span>
    </a>
  </div>
  <div>
    <a class="flex align-center" href="https://github.com/alex-shpak/hugo-book/edit/main/exampleSite/content.en/_index.md" target="_blank" rel="noopener">
      <img src="/svg/edit.svg" class="book-icon" alt="Edit"></img>
      <span>Edit this page</span>
    </a>
  </div>
</div>
      </footer>
  <div class="book-comments">
</div>
    </div>
    <aside class="book-toc">
      <div class="book-toc-content">
<nav id="TableOfContents">
  <ul>
    <li><a href="#acerbo-datus-maxime">Acerbo datus maxime</a>
      <ul>
        <li><a href="#tempora-nisi-nunc">Tempora nisi nunc</a></li>
        <li><a href="#locis-suis-novi-cum-suoque-decidit-eadem">Locis suis novi cum suoque decidit eadem</a></li>
      </ul>
    </li>
  </ul>
</nav>
      </div>
    </aside>
  </main>
<button style="position: fixed; top: 10px; right: 10px; z-index: 999;">Run Me</button></body>
""",
"""
<body dir="ltr">
  <main class="container flex">
    <aside class="book-menu">
      <div class="book-menu-content">
  <nav>
<h2 class="book-brand">
  <a class="flex align-center" href="/"><span>Hugo Book</span>
  </a>
</h2>
<div class="book-search">
  <input type="text" id="book-search-input" placeholder="Search" aria-label="Search" maxlength="64" data-hotkeys="s/"></input>
  <ul id="book-search-results"></ul>
</div>
<ul class="book-languages">
  <li>
    <input type="checkbox" id="languages" class="toggle"></input>
    <label for="languages" class="flex justify-between">
      <a role="button" class="flex align-center">
        <img src="/svg/translate.svg" class="book-icon" alt="Languages"></img>
        English
      </a>
    </label>
  </li>
</ul>
  <ul>
        <li class="book-section-flat">
    <a href="/docs/example/">Example Site</a>
  <ul>
        <li>
    <a href="/docs/example/table-of-contents/">Table of Contents</a>
  <ul>
        <li>
    <a href="/docs/example/table-of-contents/with-toc/">With ToC</a>
        </li>
        <li>
    <a href="/docs/example/table-of-contents/without-toc/">Without ToC</a>
        </li>
  </ul>
        </li>
        <li>
    <input type="checkbox" id="section-4e46b01272d410b3a99461d79326ddf4" class="toggle"></input>
    <label for="section-4e46b01272d410b3a99461d79326ddf4" class="flex justify-between">
      <a role="button">Collapsed</a>
    </label>
  <ul>
        <li>
    <a href="/docs/example/collapsed/3rd-level/">3rd Level</a>
  <ul>
        <li>
    <a href="/docs/example/collapsed/3rd-level/4th-level/">4th Level</a>
        </li>
  </ul>
        </li>
  </ul>
        </li>
  </ul>
        </li>
        <li class="book-section-flat">
    <span>Shortcodes</span>
  <ul>
        <li>
    <a href="/docs/shortcodes/buttons/">Buttons</a>
        </li>
        <li>
    <a href="/docs/shortcodes/columns/">Columns</a>
        </li>
        <li>
    <a href="/docs/shortcodes/details/">Details</a>
        </li>
        <li>
    <a href="/docs/shortcodes/expand/">Expand</a>
        </li>
        <li>
    <a href="/docs/shortcodes/hints/">Hints</a>
        </li>
        <li>
    <a href="/docs/shortcodes/katex/">Katex</a>
        </li>
        <li>
    <a href="/docs/shortcodes/mermaid/">Mermaid</a>
        </li>
        <li>
    <input type="checkbox" id="section-d3fc1bf6d66cd84b896a0af9f40cb1d5" class="toggle"></input>
    <label for="section-d3fc1bf6d66cd84b896a0af9f40cb1d5" class="flex justify-between">
      <a href="/docs/shortcodes/section/">Section</a>
    </label>
        </li>
        <li>
    <a href="/docs/shortcodes/tabs/">Tabs</a>
        </li>
  </ul>
        </li>
  </ul>
<ul>
  <li>
    <a href="/posts/">
        Blog
      </a>
  </li>
  <li>
    <a href="https://github.com/alex-shpak/hugo-book" target="_blank" rel="noopener">
        Github
      </a>
  </li>
  <li>
    <a href="https://themes.gohugo.io/hugo-book/" target="_blank" rel="noopener">
        Hugo Themes
      </a>
  </li>
</ul>
</nav>
      </div>
    </aside>
    <div class="book-page">
  <article class="markdown"><h1 id="acerbo-datus-maxime">
  Acerbo datus maxime
  <a class="anchor" href="#acerbo-datus-maxime">#</a>
</h1>
<div class="book-columns flex flex-wrap">
  <div class="flex-even markdown-inner">
    <h2 id="astris-ipse-furtiva">
  Astris ipse furtiva
  <a class="anchor" href="#astris-ipse-furtiva">#</a>
</h2>
<p>Est in vagis et Pittheus tu arge accipiter regia iram vocatur nurus. Omnes ut
olivae sensit <strong>arma sorori</strong> deducit, inesset <strong>crudus</strong>, ego vetuere aliis,
modo arsit? Utinam rapta fiducia valuere litora <em>adicit cursu</em>, ad facies
  </p></div>
  <div class="flex-even markdown-inner">
    <h2 id="suis-quot-vota">
  Suis quot vota
  <a class="anchor" href="#suis-quot-vota">#</a>
</h2>
<p>Ea <em>furtique</em> risere fratres edidit terrae magis. Colla tam mihi tenebat:
miseram excita suadent es pecudes iam. Concilio <em>quam</em> velatus posset ait quod
nunc! Fragosis suae dextra geruntur functus vulgata.
  </p></div>
</div>
<h2 id="tempora-nisi-nunc">
  Tempora nisi nunc
  <a class="anchor" href="#tempora-nisi-nunc">#</a>
</h2>
<p>Lorem <strong>markdownum</strong> emicat gestu. Cannis sol pressit ducta. <strong>Est</strong> Idaei,
tremens ausim se tutaeque, illi ulnis hausit, sed, lumina cutem. Quae avis
sequens!</p>
<pre><code>var panel = ram_design;
if (backup + system) {
    file.readPoint = network_native;
    sidebar_engine_device(cell_tftp_raster,
            dual_login_paper.adf_vci.application_reader_design(
            graphicsNvramCdma, lpi_footer_snmp, integer_model));
}
</code></pre>
<h2 id="locis-suis-novi-cum-suoque-decidit-eadem">
  Locis suis novi cum suoque decidit eadem
  <a class="anchor" href="#locis-suis-novi-cum-suoque-decidit-eadem">#</a>
</h2>
<p>Idmoniae ripis, at aves, ali missa adest, ut <em>et autem</em>, et ab?</p>
</article>
      <footer class="book-footer">
  <div class="flex flex-wrap justify-between">
  <div><a class="flex align-center" href="https://github.com/alex-shpak/hugo-book/commit/9013a1f4570885416254aabbe7e389822d2fb215" title="Last modified by Alex Shpak | November 2, 2022" target="_blank" rel="noopener">
      <img src="/svg/calendar.svg" class="book-icon" alt="Calendar"></img>
      <span>November 2, 2022</span>
    </a>
  </div>
  <div>
    <a class="flex align-center" href="https://github.com/alex-shpak/hugo-book/edit/main/exampleSite/content.en/_index.md" target="_blank" rel="noopener">
      <img src="/svg/edit.svg" class="book-icon" alt="Edit"></img>
      <span>Edit this page</span>
    </a>
  </div>
</div>
      </footer>
  <div class="book-comments">
</div>
    </div>
    <aside class="book-toc">
      <div class="book-toc-content">
<nav id="TableOfContents">
  <ul>
    <li><a href="#acerbo-datus-maxime">Acerbo datus maxime</a>
      <ul>
        <li><a href="#tempora-nisi-nunc">Tempora nisi nunc</a></li>
        <li><a href="#locis-suis-novi-cum-suoque-decidit-eadem">Locis suis novi cum suoque decidit eadem</a></li>
      </ul>
    </li>
  </ul>
</nav>
      </div>
    </aside>
  </main>
<button style="position: fixed; top: 10px; right: 10px; z-index: 999;">Run Me</button></body>
"""
)
]