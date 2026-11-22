class Solution {
    public double[] convertTemperature(double celsius) {
        double kelvin = celsius+273.15d;
        double F = celsius*1.80+32.00d;
        return new double[]{kelvin,F};
        
    }
}