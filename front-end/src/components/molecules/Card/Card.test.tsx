import { render, screen } from "@testing-library/react";
import { Card } from "./Card";
import { INewsItem } from "../../../models";

describe("Card", () => {
  it("renders the card with news items", () => {
    const mockNews: INewsItem[] = [
      {
        number: 1,
        title: "News Title 1",
        points: 100,
        number_of_comments: 50,
      },
      {
        number: 2,
        title: "News Title 2",
        points: 80,
        number_of_comments: 30,
      },
    ];

    render(<Card sortedNews={mockNews} />);

    expect(screen.getByText("News Title 1")).toBeInTheDocument();
    expect(screen.getByText("News Title 2")).toBeInTheDocument();
    expect(screen.getByTestId("card")).toBeInTheDocument();
    expect(screen.getByTestId("NestedList-Container")).toBeInTheDocument();
  });
});
