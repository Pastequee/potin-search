"use client";
import { MagnifyingGlassIcon } from "@radix-ui/react-icons";
import { Input } from "./ui/input";
import { FormEvent, useRef } from "react";

export default function SearchBar({ text }: { text: string | undefined }) {
    const inputRef = useRef<HTMLInputElement>(null);
    const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        window.location.href = "/?q=" + inputRef.current?.value;
    };
    return (
        <form className="relative mt-10 w-[500px]" onSubmit={handleSubmit}>
            <span className="absolute inset-y-0 left-3 flex items-center pointer-events-none">
                <MagnifyingGlassIcon className="h-8 w-8 text-gray-300" />
            </span>
            <Input
                type="text"
                required
                ref={inputRef}
                defaultValue={text || ""}
                placeholder="Search for a juicy potin"
                className="text-xl pl-14 rounded-full"
            />
        </form>
    );
}
