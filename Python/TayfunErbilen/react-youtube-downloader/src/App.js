import { useState, useEffect, useRef } from "react";
import YoutubeVideo from "./YoutubeVideo";
import History from "./History";

function App() {
  const isDownloadable = useRef(false)
  const [url, setUrl] = useState("");
  const [history, setHistory] = useState(
    localStorage.getItem("history")
      ? JSON.parse(localStorage.getItem("history"))
      : []
  );
  const [youtube, setYoutube] = useState(false);
  const [loading, setLoading] = useState(false);

  const clearHistory = () => {
    setHistory([])
  }

  const downloadAgain = (url) => {
    isDownloadable.current = true
    setUrl(url)
  }

  const clickHandle = () => {
    isDownloadable.current = true
    download()
  }

  useEffect(() => {
    if (isDownloadable.current === true){
      download()
    }
  }, [url])

  useEffect(() => {
    if (youtube) {
      if (!history.find((h) => h.url === url)) {
        let newHistory = {
          url: url,
          title: youtube.info.title,
        };
        setHistory([...history, newHistory]);
      }
    }
  }, [youtube]);

  useEffect(() => {
    localStorage.setItem("history", JSON.stringify(history));
  }, [history]);

  const download = () => {
    if (url) {
      setLoading(true);
      fetch(`https://prototurk.pythonanywhere.com/api/youtube?url=${url}`)
        .then((res) => res.json())
        .then((data) => {
          setLoading(false);
          setYoutube(data);
        });
    }
  };

  return (
    <div className="App">
      <form action="" method="post" onSubmit={(e) => e.preventDefault()}>
        <img src="/youtube.svg" height="100px" />
        <h3>Youtube Downloader</h3>
        <div className="search">
          <input
            type="text"
            onFocus={() => isDownloadable.current = false}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Youtube URL"
          />
          <button type="submit" onClick={clickHandle}>
            Download
          </button>
        </div>
      </form>
      {loading && <div className="loader">Yükleniyor..</div>}
      {youtube && loading === false && <YoutubeVideo youtube={youtube} />}
      {history.length > 0 && <History list={history} downloadAgain={downloadAgain} clearHistory={clearHistory} />}
    </div>
  );
}

export default App;
