const sourceArchives = new Map();
const archiveImageUrls = new Map();

async function archiveImageUrl({archiveUrl, start, length, method, member}) {
  if (!sourceArchives.has(archiveUrl)) {
    sourceArchives.set(archiveUrl, fetch(archiveUrl).then(response => {
      if (!response.ok) throw new Error('Source archive request failed');
      return response.arrayBuffer();
    }).catch(error => {
      sourceArchives.delete(archiveUrl);
      throw error;
    }));
  }
  const archive = await sourceArchives.get(archiveUrl);
  const from = Number(start);
  const to = from + Number(length);
  if (to > archive.byteLength) throw new Error('Image exceeds archive bounds');
  const stored = new Blob([archive.slice(from, to)]);
  const payload = method === '0' ? stored : await new Response(
    stored.stream().pipeThrough(new DecompressionStream('deflate-raw'))
  ).blob();
  return URL.createObjectURL(new Blob([payload], {type: 'image/jpeg'}));
}

function loadArchiveImages(card) {
  card.querySelectorAll('img[data-archive-url]:not([src]):not([data-loading])').forEach(async img => {
    img.dataset.loading = 'true';
    const {archiveUrl, member} = img.dataset;
    const key = archiveUrl + '#' + member;
    try {
      if (!archiveImageUrls.has(key)) {
        archiveImageUrls.set(key, archiveImageUrl(img.dataset).catch(error => {
          archiveImageUrls.delete(key);
          throw error;
        }));
      }
      const url = await archiveImageUrls.get(key);
      img.src = url;
      img.parentElement.href = url;
      const link = card.querySelector(`[data-image="${img.id}"]`);
      link.href = url;
      link.textContent = link.textContent.replace('official archive', 'original image');
    } catch {
      img.alt = 'Image unavailable. Open the official archive to view it.';
    } finally {
      delete img.dataset.loading;
    }
  });
}
