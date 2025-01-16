import Potin, { PotinType } from "@/components/potin";
import SearchBar from "@/components/searchBar";
import { join } from "path";

export default async function Home({
    searchParams,
}: {
    searchParams: Promise<{ [key: string]: string | undefined }>;
}) {
    const { q } = await searchParams;
    const data = await fetch(
        join(
            process.env.FLASK_API_URL || "http://localhost:5000",
            "search?query=" + (q || "")
        )
    );
    const potins: PotinType[] = await data.json();

    return (
        <main className="flex flex-col items-center mt-20">
            <h1 className="text-7xl font-bold">
                <span className="text-blue-600">P</span>
                <span className="text-red-500">o</span>
                <span className="text-yellow-400">t</span>
                <span className="text-blue-600">i</span>
                <span className="text-green-600">n</span>{" "}
                <span className="text-red-500">S</span>
                <span className="text-blue-600">e</span>
                <span className="text-yellow-400">a</span>
                <span className="text-green-600">r</span>
                <span className="text-red-500">c</span>
                <span className="text-blue-600">h</span>
            </h1>
            <SearchBar text={q} />
            <section className="flex flex-col gap-4 mt-10">
                {potins.map((potin, idx) => (
                    <a key={idx} href={potin.url} target="_blank">
                        <Potin data={potin} />
                    </a>
                ))}
            </section>
        </main>
    );
}
