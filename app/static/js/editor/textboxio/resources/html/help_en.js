/** @license
 * Copyright (c) 2013-2016 Ephox Corp. All rights reserved.
 * This software is provided "AS IS," without a warranty of any kind.
 */
!function () {
  var a = function (a) {
    return function () {
      return a
    }
  }, b = function (a, b) {
    return a.src.indexOf(b) === a.src.length - b.length
  }, c = function (a) {
    for (var b = a.split("."), c = window, d = 0; d < b.length && void 0 !== c && null !== c; ++d)c = c[b[d]];
    return c
  }, d = function (a, d) {
    for (var e, f = document.getElementsByTagName("script"), g = 0; g < f.length; g++)if (e = b(f[g], a)) {
      var h = f[g].getAttribute("data-main");
      if (void 0 === h)throw"no data-main attribute found on " + d + " script tag";
      f[g].removeAttribute("data-main");
      var i = c(h);
      if ("function" != typeof i)throw"attribute on " + d + " does not reference a global method";
      return i
    }
    throw"cannot locate " + d + " script tag"
  }, e = d("help_en.js", "help for language en");
  e({
    about: a('<div class="ephox-polish-help-article ephox-polish-help-about">\n  <div role="heading" aria-level="1" class="ephox-polish-help-h1">About</div>\n  <p>Textbox.io is a WYSIWYG tool for creating great looking content in online apps. Whether it\u2019s in social communities, blogs, emails, or anything in between, Textbox.io lets people express themselves on the web.</p>\n  <p>&nbsp;</p>\n  <p>Textbox.io @@FULL_VERSION@@</p>\n  <p>Client build @@CLIENT_VERSION@@</p>\n  <p class="ephox-polish-help-integration">Integration for @@INTEGRATION_TYPE@@, version @@INTEGRATION_VERSION@@</p>\n  <p>&nbsp;</p>\n  <p>Copyright 2016 Ephox Corporation. All rights reserved.</p>\n  <p><a class="ephox-license-link" href="javascript:void(0)">Third Party Licenses</a></p>\n</div>\n'),
    accessibility: a('<div class="ephox-polish-help-article">\n  <div role="heading" aria-level="1" class="ephox-polish-help-h1">Keyboard Navigation</div>\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">Activating Keyboard Navigation</div>\n  <p>To enable keyboard navigation on the toolbar, press F10 for Windows or ALT + F10 on Mac OSX.  The first item on the toolbar will be highlighted with a blue outline indicating a selected state. </p>\n\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">Moving Between Groups</div>\n  <p>The buttons within the toolbar are separated by groups of similar actions.  When keyboard navigation is active, pressing the tab key will move the selection to the next group while shift + tab will move the selection back to the previous group.  Pressing tab on the last group will cycle back to the first group of buttons.</p>\n\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">Moving Between Items or Buttons</div>\n  <p>To move back and forth between items, use the arrow keys.  Items will cycle within their groups, to jump to the next group press tab and use the arrow keys to traverse the group.</p>\n\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">Executing Commands</div>\n  <p>To execute a command, navigate the selection to the desired button and hit space or enter.</p>\n\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">Opening, Navigating and Closing Menus</div>\n  <p>When a toolbar button contains a menu, pressing space or enter will open the menu. When the menu opens the first item will be selected,  use the arrow keys to navigate the menu.  To move up or down the menu, press the up or down arrow key respectively, this is the same for submenus.</p>\n\n  <p>Menu items that have submenus are denoted by a chevron symbol.  Using the arrow key that corresponds to the direction of the chevron will expand the submenu, while the arrow key in the opposite direction will close the submenu.</p>\n\n  <p>To close any active menu, hit the escape key.  When a menu is closed the selection will be restored to its previous selection.</p>\n\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">Editing or Removing Hyperlinks</div>\n\n  <p>To edit or remove a link, navigate to the Insert menu, and select Insert Link. The editor displays the edit link dialog. </p>\n\n  <p>Edit the link by entering the new url in the update link input box and pressing enter. Remove the link from the document by choosing the remove button. To exit the dialog without making changes press esc.</p>\n\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">Changing Font Sizes &amp; Table Border Size</div>\n\n  <p>Change font sizes by navigating to the font menu and selecting font size. The editor displays the size dialog in the menu and sets the focus to the dialog.</p>\n\n  <p>Change border sizes by navigating to the table border size toolbar item and selecting table border size. The editor displays the size dialog in the menu and sets the focus to the dialog. Note: The table border size toolbar item is only available when the cursor is within a table.</p>\n\n  <p>Within the size dialog, press the tab key to move the selection to the next control. Press shift+tab to move the selection to the previous control.</p>\n\n  <p>Modify the size by entering the new value in the size input box. For example, 14px or 1em. To submit changes, press enter. Note that pressing enter closes the dialog and returns the focus to the document.</p>\n\n  <p>Change the size without exiting the dialog by activating the increase size or decrease size buttons. Changing the size with the increase or decrease buttons will immediately change the selected element\'s size while maintaining the current unit value. Exit the size dialog by pressing esc.</p>\n\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">Cropping an Image</div>\n\n  <p>To access the crop feature, select an image to show the image operations on the toolbar. These operations are also available in the context menu. Once crop is activated, a crop mask will be positioned on top of the image and the top left corner will be selected.</p>\n\n  <p>Navigate using tab. Each of the 4 corners can be selected as well as the overall crop mask box. Each corner can be positioned individually or all corners can be moved at the same time by moving the overall crop mask box.</p>\n\n  <p>Moving the selection across the image is done with the arrow keys. Each press of an arrow key will move by 10 pixels, for smaller movements hold shift while pressing an arrow key to move one pixel.</p>\n\n  <p>To apply the crop to the image press enter.</p>\n\n  <p>To cancel the crop action with no effects on the image, press the ESC key.</p>\n\n  <table role="grid" aria-readonly="true" cellpadding="0" cellspacing="0" class="ephox-polish-tabular ephox-polish-help-table ephox-polish-help-table-shortcuts">\n      <caption>Keyboard Navigation</caption>\n      <thead>\n        <tr role="row">\n          <th role="columnheader" scope="col">Action</th>\n          <th role="columnheader" scope="col">Windows</th>\n          <th role="columnheader" scope="col">Mac OS</th>\n        </tr>\n      </thead>\n      <tbody>\n      <tr role="row">\n        <td role="gridcell">Activate Toolbar</td>\n        <td role="gridcell">F10</td>\n        <td role="gridcell">ALT + F10</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Select Next/Prev Group Button</td>\n        <td role="gridcell">\u2190 or \u2192</td>\n        <td role="gridcell">\u2190 or \u2192</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Move to Next Group</td>\n        <td role="gridcell">TAB</td>\n        <td role="gridcell">TAB</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Move to Previous Group</td>\n        <td role="gridcell">SHIFT + TAB</td>\n        <td role="gridcell">SHIFT + TAB</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Execute Command</td>\n        <td role="gridcell">SPACE or ENTER</td>\n        <td role="gridcell">SPACE or ENTER</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Open Main Menu</td>\n        <td role="gridcell">SPACE or ENTER</td>\n        <td role="gridcell">SPACE or ENTER</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Open/Expand Submenu</td>\n        <td role="gridcell">SPACE or ENTER or \u2192</td>\n        <td role="gridcell">SPACE or ENTER or \u2192</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Select Next/Prev Menu Item</td>\n        <td role="gridcell">\u2193 or \u2191</td>\n        <td role="gridcell">\u2193 or \u2191</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Close menu</td>\n        <td role="gridcell">ESC</td>\n        <td role="gridcell">ESC</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Close/Collapse Submenu</td>\n        <td role="gridcell">ESC or \u2190</td>\n        <td role="gridcell">ESC or \u2190</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Move Image Crop selection</td>\n        <td role="gridcell">\u2190 or  \u2192 or \u2193 or \u2191</td>\n        <td role="gridcell">\u2190 or  \u2192 or \u2193 or \u2191</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Precisely Move Image Crop selection</td>\n        <td role="gridcell">Hold SHIFT while moving</td>\n        <td role="gridcell">Hold SHIFT while moving</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Apply Crop</td>\n        <td role="gridcell">ENTER</td>\n        <td role="gridcell">ENTER</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Cancel Crop</td>\n        <td role="gridcell">ESC</td>\n        <td role="gridcell">ESC</td>\n      </tr>\n    </tbody>\n  </table>\n</div>\n'),
    a11ycheck: a('<div class="ephox-polish-help-article">\n  <div role="heading" aria-level="1" class="ephox-polish-help-h1">Accessibility Checking</div>\n  <p>The Accessibility Checking tool (if enabled) can identify the following accessibility issues in HTML documents.</p>\n  <table role="grid" aria-readonly="true" cellpadding="0" cellspacing="0" class="ephox-polish-tabular ephox-polish-a11ycheck-table">\n      <caption>Issue Definitions</caption>\n      <thead>\n        <tr role="row">\n          <th role="columnheader" scope="col">Issue</th>\n          <th role="columnheader" scope="col">WCAG</th>\n          <th role="columnheader" scope="col">Description</th>\n        </tr>\n      </thead>\n      <tbody>\n      <tr role="row">\n        <td role="gridcell">Images must have an alternative text description</td>\n        <td role="gridcell">1.1.1</td>\n        <td role="gridcell">Images must have an alternative text value set, describing the image subject to users with impaired vision. </td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Alternative text must not be the same as the image filename</td>\n        <td role="gridcell">1.1.1</td>\n        <td role="gridcell">Avoid use of the image filename in alternative text value. Choose an alternative text value that describes the subject of the image.</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Tables must have captions</td>\n        <td role="gridcell">1.3.1</td>\n        <td role="gridcell">Tables should have brief descriptive text that indicates the contents of the table.</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Complex tables should have summaries</td>\n        <td role="gridcell">1.3.1</td>\n        <td role="gridcell">Tables with complex structures (cells spanning multiple rows or columns) should include a summary that describes the table structure. </td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Table caption and summary cannot have the same value</td>\n        <td role="gridcell">1.3.1</td>\n        <td role="gridcell">Table caption should describe the contents of the table, whereas table summary should describe the structure of complex tables. </td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Tables must have at least one header cell</td>\n        <td role="gridcell">1.3.1</td>\n        <td role="gridcell">Tables should include appropriate row or column headers that describe the contents of the row or column.<br/><a href="http://webaim.org/techniques/tables/data#th" target="_blank">More info on this topic (webaim.org).</a> </td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Table headers must be applied to a row or a column</td>\n        <td role="gridcell">1.3.1</td>\n        <td role="gridcell">Tables headers must be associated with the row or column that they describe.<br/><a href="http://webaim.org/techniques/tables/data#th" target="_blank">More info on this topic (webaim.org).</a> </td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">This paragraph looks like a heading. If it is a heading, please select a heading level.</td>\n        <td role="gridcell">1.3.1</td>\n        <td role="gridcell">Use headings to separate documents into sections. Avoid use of formatted paragraphs in place of headings.<br/><a href="http://webaim.org/techniques/semanticstructure/#correctly" target="_blank">More info on this topic (webaim.org).</a> </td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Headings must be applied in sequential order. For example: Heading 1 should be followed by Heading 2, not Heading 3.</td>\n        <td role="gridcell">1.3.1</td>\n        <td role="gridcell">Subsequent document headings should appear hierarchically, appearing in ascending or equivalent order.<br/><a href="http://webaim.org/techniques/semanticstructure/#contentstructure" target="_blank">More info on this topic (webaim.org).</a> </td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Use list markup for lists</td>\n        <td role="gridcell">1.3.1</td>\n        <td role="gridcell">Ensure that lists of items use HTML list structure to represent lists (<code>&lt;ul&gt;</code> or <code>&lt;ol&gt;</code> &amp; <code>&lt;li&gt;</code>).</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Text must have a contrast ratio of 4.5:1</td>\n        <td role="gridcell">1.4.3</td>\n        <td role="gridcell">Text and its background must have a contrast ratio such that it can be read by people with moderately low vision.</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Adjacent links should be merged.</td>\n        <td role="gridcell">2.4.4</td>\n        <td role="gridcell">Adjacent hyperlinks pointing to the same resource should be merged into a single hyperlink.</td>\n      </tr>\n    </tbody>\n  </table>\n  <div role="heading" aria-level="2" class="ephox-polish-help-h2">More Information</div>\n  <p>\n    <a href="http://webaim.org/intro/" target="_blank">Introduction to web accessibility (webaim.org)</a> <br/>\n    <a href="http://www.w3.org/WAI/intro/wcag" target="_blank">Introduction to WCAG 2.0 (w3.org)</a> <br/>\n    <a href="http://www.section508.gov/" target="_blank">Section 508 of the US Rehabilitation Act (section508.gov)</a>\n  </p>\n</div>'),
    markdown: a('<div class="ephox-polish-help-article">\n  <div role="heading" aria-level="1" class="ephox-polish-help-h1">Markdown Formatting</div>\n  <p>Markdown is a syntax for creating HTML structures and formatting without having to use keyboard shortcuts or access menus. To use markdown formatting, enter the desired syntax followed by the enter or space key.</p>\n  <table role="grid" aria-readonly="true" cellpadding="0" cellspacing="0" class="ephox-polish-tabular ephox-polish-help-table ephox-polish-help-table-markdown">\n      <caption>Keyboard Formatting Syntax</caption>\n      <thead>\n        <tr role="row">\n          <th role="columnheader" scope="col">Syntax</th>\n          <th role="columnheader" scope="col">HTML Result</th>\n        </tr>\n      </thead>\n      <tbody>\n      <tr role="row">\n        <td role="gridcell"><pre># Largest Heading</pre></td>\n        <td role="gridcell"><pre>&lt;h1&gt;Largest Heading&lt;/h1&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>## Larger Heading</pre></td>\n        <td role="gridcell"><pre>&lt;h2&gt;Larger Heading&lt;/h2&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>### Large Heading</pre></td>\n        <td role="gridcell"><pre>&lt;h3&gt;Large Heading&lt;/h3&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>####  Heading</pre></td>\n        <td role="gridcell"><pre>&lt;h4&gt;Heading&lt;/h4&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>##### Small Heading</pre></td>\n        <td role="gridcell"><pre>&lt;h5&gt;Small Heading&lt;/h5&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>###### Smallest Heading</pre></td>\n        <td role="gridcell"><pre>&lt;h6&gt;Smallest Heading&lt;/h6&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>* Unordered list</pre></td>\n        <td role="gridcell"><pre>&lt;ul&gt;&lt;li&gt;Unordered List&lt;/li&gt;&lt;/ul&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>1. Ordered list</pre></td>\n        <td role="gridcell"><pre>&lt;ol&gt;&lt;li&gt;Ordered List&lt;/li&gt;&lt;/ol&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>*Italic*</pre></td>\n        <td role="gridcell"><pre>&lt;em&gt;Italic&lt;/em&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>**Bold**</pre></td>\n        <td role="gridcell"><pre>&lt;strong&gt;Bold&lt;/strong&gt;</pre></td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell"><pre>---</pre></td>\n        <td role="gridcell"><pre>&lt;hr/&gt;</pre></td>\n      </tr>\n    </tbody>\n  </table>\n</div>\n'),
    shortcuts: a('<div class="ephox-polish-help-article">\n  <div role="heading" aria-level="1" class="ephox-polish-help-h1">Keyboard Shortcuts</div>\n  <table role="grid" aria-readonly="true" cellpadding="0" cellspacing="0" class="ephox-polish-tabular ephox-polish-help-table ephox-polish-help-table-shortcuts">\n    <caption>Editor Commands</caption>\n    <thead>\n      <tr role="row">\n        <th role="columnheader" scope="col">Action</th>\n        <th role="columnheader" scope="col">Windows</th>\n        <th role="columnheader" scope="col">Mac OS</th>\n      </tr>\n    </thead>\n    <tbody>\n      <tr role="row">\n        <td role="gridcell">Undo</td>\n        <td role="gridcell">CTRL + Z</td>\n        <td role="gridcell">\u2318Z</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Redo</td>\n        <td role="gridcell">CTRL + Y</td>\n        <td role="gridcell">\u2318\u21e7Z</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Bold</td>\n        <td role="gridcell">CTRL + B</td>\n        <td role="gridcell">\u2318B</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Italic</td>\n        <td role="gridcell">CTRL + I</td>\n        <td role="gridcell">\u2318I</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Underline</td>\n        <td role="gridcell">CTRL + U</td>\n        <td role="gridcell">\u2318U</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Indent</td>\n        <td role="gridcell">CTRL + ]</td>\n        <td role="gridcell">\u2318]</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Decrease Indent</td>\n        <td role="gridcell">CTRL + [</td>\n        <td role="gridcell">\u2318[</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Add Link</td>\n        <td role="gridcell">CTRL + K</td>\n        <td role="gridcell">\u2318K</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Find</td>\n        <td role="gridcell">CTRL + F</td>\n        <td role="gridcell">\u2318F</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Full Screen Mode (Toggle)</td>\n        <td role="gridcell">CTRL + SHIFT + F</td>\n        <td role="gridcell">\u2318\u21e7F</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Help Dialog (Open)</td>\n        <td role="gridcell">CTRL + SHIFT + H</td>\n        <td role="gridcell">\u2303\u2325H</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Context Menu (Open)</td>\n        <td role="gridcell">SHIFT + F10</td>\n        <td role="gridcell">\u21e7F10\u200e\u200f</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Code Autocomplete</td>\n        <td role="gridcell">CTRL + Space</td>\n        <td role="gridcell">\u2303Space</td>\n      </tr>\n      <tr role="row">\n        <td role="gridcell">Accessible Code View</td>\n        <td role="gridcell">CTRL + SHIFT + U</td>\n        <td role="gridcell">\u2318\u2325U</td>\n      </tr>\n    </tbody>\n  </table>\n  <div class="ephox-polish-help-note" role="note">*Note: Some features can be disabled by your administrator.</div>\n</div>\n')
  })
}();