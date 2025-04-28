import { useState } from "react";
import "./App.css";

import {Stack, LinearProgress} from "@mui/material";

import { getNewsByComments, getNewsByPoints } from "./services/news.service";
import { INewsItem } from "./models";

import { Button } from "./components/atoms/Button";
import { Card } from "./components/molecules/Card";

function App() {
  const [sortedNews, setsortedNews] = useState<INewsItem[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  return (
    <>
      <Stack
        direction="row"
        spacing={2}
        justifyContent="center"
        alignItems="center"
        sx={{ margin: "20px" }}
        >
        <Button
          variant="contained"
          text="Sort by Comments"
          onClick={async () => {
            setIsLoading(true);
            const newsByComments = await getNewsByComments();
            setsortedNews(newsByComments);
            setIsLoading(false);
          }}/>
        <Button
          variant="contained"
          text="Sort by Points"
          onClick={async () => {
            setIsLoading(true);
            const newsByPoints = await getNewsByPoints();
            setsortedNews(newsByPoints);
            setIsLoading(false);
          }}/>
        </Stack>
        {isLoading && <LinearProgress/>}
      <Card sortedNews={sortedNews} />
    </>
  );
}

export default App;
