import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "./ui/card";

export interface PotinType {
    url: string;
    title: string;
    content: string;
    summary: string;
    author: string;
}

interface PotinProps {
    data: PotinType;
}

export default function Potin({ data }: PotinProps) {
    return (
        <article>
            <Card className="w-[840px] bg-white shadow-lg rounded-lg overflow-hidden">
                <CardHeader className="px-6 py-4">
                    <CardTitle className="text-xl font-semibold text-gray-800">
                        {data.title}
                    </CardTitle>
                    <CardDescription className="text-sm text-gray-500 mt-2">
                        By {data.author}
                    </CardDescription>
                </CardHeader>
                <CardContent className="px-6 py-4">
                    <p className="text-gray-700 text-sm">{data.summary}</p>
                </CardContent>
            </Card>
        </article>
    );
}
