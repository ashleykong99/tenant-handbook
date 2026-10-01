/* Tenant handbook — global search */
(function () {
  var idx = window.SEARCH_INDEX || [];
  var wrap = document.querySelector('.search-wrap');
  if (!wrap) return;
  var input = wrap.querySelector('.search-input');
  var panel = wrap.querySelector('.search-results');

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function search(v) {
    v = v.toLowerCase();
    var hits = [];
    for (var i = 0; i < idx.length; i++) {
      var it = idx[i];
      var hay = (it.q + ' ' + it.t + ' ' + it.cat + ' ' + (it.kw || '')).toLowerCase();
      if (hay.indexOf(v) >= 0) {
        hits.push(it);
        if (hits.length >= 15) break;
      }
    }
    return hits;
  }

  function render(hits) {
    if (!hits.length) {
      panel.innerHTML = '<div class="sr-empty">没有找到相关问题，换个词试试</div>';
    } else {
      panel.innerHTML = hits.map(function (h) {
        return '<a class="sr-item" href="' + h.file + '#' + h.id + '">' +
          '<span class="sr-cat">' + esc(h.cat) + '</span>' +
          '<span class="sr-q">' + esc(h.q) + '</span>' +
          '</a>';
      }).join('');
    }
    panel.style.display = 'block';
  }

  input.addEventListener('input', function () {
    var v = input.value.trim();
    if (v.length < 1) {
      panel.innerHTML = '';
      panel.style.display = 'none';
      return;
    }
    render(search(v));
  });

  input.addEventListener('focus', function () {
    if (input.value.trim().length >= 1) render(search(input.value.trim()));
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.search-wrap')) panel.style.display = 'none';
  });
})();

/* Deep-link: open + scroll to a question when landing with #qN */
(function () {
  var h = location.hash;
  if (h && h.length > 1) {
    var el = document.querySelector(h);
    if (el && el.tagName === 'DETAILS') {
      el.open = true;
      setTimeout(function () {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 200);
    }
  }
})();
