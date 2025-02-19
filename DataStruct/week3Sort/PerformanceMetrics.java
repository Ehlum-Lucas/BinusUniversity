public class PerformanceMetrics {
    public static void measureRuntime(Runnable function) {
        System.gc();
        long startTime = System.nanoTime();

        Runtime runtime = Runtime.getRuntime();
        long memoryBefore = runtime.totalMemory() - runtime.freeMemory();

        function.run();

        long memoryAfter = runtime.totalMemory() - runtime.freeMemory();
        long endTime = System.nanoTime();

        long timeTaken = (endTime - startTime) / 1_000_000;
        long memoryUsed = Math.max(0, memoryAfter - memoryBefore);

        System.out.println("Time taken: " + timeTaken + " ms");
        System.out.println("Memory used: " + memoryUsed + " bytes");
    }

}
