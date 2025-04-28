import { useState } from "react";
import "./App.css";

import Stack from "@mui/material/Stack";

import { getNewsByComments, getNewsByPoints } from "./services/news.service";
import { INewsItem } from "./models";

import { Button } from "./components/atoms/Button";
import { Card } from "./components/molecules/Card";

function App() {
  const [sortedNews, setsortedNews] = useState<INewsItem[]>([]);

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
            const newsByComments = await getNewsByComments();
            setsortedNews(newsByComments);
          }}/>
        <Button
          variant="contained"
          text="Sort by Points"
          onClick={async () => {
            const newsByPoints = await getNewsByPoints();
            setsortedNews(newsByPoints);
          }}/>
        </Stack>
      <Card sortedNews={sortedNews} />
    </>
  );
}

export default App;
