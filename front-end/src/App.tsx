import { useEffect, useState } from 'react'
import './App.css'

import { getNewsByComments, getNewsByPoints } from './services/news.service'
import { INewsItem } from './models'

function App() {
  // const [newsByComments, setNewsByComments] = useState<INewsItem[]>([]);
  const [newsByPoints, setNewsByPoints] = useState<INewsItem[]>([]);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        // const newsByComments = await getNewsByComments();
        // setNewsByComments(newsByComments);
        const newsByPoints = await getNewsByPoints();
        setNewsByPoints(newsByPoints);
      } catch (error) {
        console.error('Error fetching news from service:', error);
      }
    }
    fetchNews();
  }, []);

  return (
    <>
      <div>
            <h1>News by Comments</h1>
            <ul>
                {/* {newsByComments.map((item) => ( */}
                {newsByPoints.map((item) => (
                    <li key={item.number}>
                        {/* {item.title} ({item.number_of_comments} comments) */}
                        {item.title} ({item.number_of_comments} points)
                    </li>
                ))}
            </ul>
        </div>
    </>
  );
};

export default App
