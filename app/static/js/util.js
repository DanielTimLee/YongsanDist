var clear = function () {
  $('.nag').nag('hide');
};
$('.ui.nav.sidebar').sidebar('attach events', '.ui.top.menu > .hamburger.item', '.back.nav.item');
$('.ui.notification.sidebar').sidebar('attach events', '.ui.top.menu > .user.menu > .notification.item', '.back.notification.item');

$('.ui.nav.sidebar').sidebar('attach events', '.nav > .back.item');
$('.ui.notification.sidebar').sidebar('attach events', '.notification > .back.item');

$('.dropdown').dropdown();
$('.nag').nag('show');
$('.close.icon').click(clear);
$(document).ready(function () {
  setTimeout(clear, 5000);
});
$('.ui.sticky')
  .sticky({
    context: 'body'
  })
;
