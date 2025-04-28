import {
  Box,
  ListItemText,
  ListItem,
  List,
  Card as MuiCard,
} from "@mui/material";

import ICardProps from "./Types";
import { cardStyle } from "./Card.styles";

export const Card: React.FC<ICardProps> = ({
  sortedNews,
}: ICardProps) => {
  return (
    <MuiCard data-testid="card" sx={cardStyle.mainContainer}>
      <List
      data-testid="NestedList-Container"
      >
        {sortedNews.map((item) => (
          <ListItem key={item.number}>
            <Box sx={cardStyle.cardContentStyle}>
              <ListItemText
                primary={item.title}
                secondary={`(${item.points} points) (${item.number_of_comments} comments)`}
              />
            </Box>
          </ListItem>
        ))}
      </List>
    </MuiCard>
  );
};
