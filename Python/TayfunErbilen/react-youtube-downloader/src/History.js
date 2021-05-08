function History({list, downloadAgain, clearHistory}){
    return (
        <div className="search-history">
            <h4>
                Arama Geçmişi
                <button onClick={clearHistory}>Geçmişi temizle</button>
            </h4>
            <ul>
                {list.map((item, key) => (
                    <li key={key} onClick={e => downloadAgain(item.url)}>
                        {item.title}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default History