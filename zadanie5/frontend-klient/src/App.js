import React, { useState, useEffect } from 'react';

const Produkty = () => {
    const [produkty, setProdukty] = useState([]);

    useEffect(() => {
        fetchProdukty();
    }, []);

    const fetchProdukty = async () => {
        try {
            const response = await fetch('http://localhost:8080/api/produkty');
            const data = await response.json();
            setProdukty(data);
        } catch (error) {
            console.error('Błąd pobierania danych:', error);
        }
    };

    return (
        <div>
            <h2>Produkty</h2>
            <ul>
                {produkty.map(produkt => (
                    <li key={produkt.id}>{produkt.nazwa}</li>
                ))}
            </ul>
        </div>
    );
};

const Platnosci = () => {
    const [kwota, setKwota] = useState(0);

    const handlePlatnosc = async () => {
        try {
            const response = await fetch('http://localhost:8080/api/platnosci', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ kwota }),
            });
            const data = await response.json();
            console.log('Odpowiedź serwera:', data);
        } catch (error) {
            console.error('Błąd wysyłania płatności:', error);
        }
    };

    return (
        <div>
            <h2>Płatności</h2>
            <input
                type="number"
                value={kwota}
                onChange={e => setKwota(e.target.value)}
            />
            <button onClick={handlePlatnosc}>Zapłać</button>
        </div>
    );
};

const App = () => {
    return (
        <div>
            <Produkty />
            <Platnosci />
        </div>
    );
};

export default App;
